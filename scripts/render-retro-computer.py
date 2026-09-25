"""Render a self-contained, looping 3D retro computer GIF with Pillow."""
from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
W, H, SCALE = 760, 560, 2
BG = '#14130e'
FONT = '/System/Library/Fonts/Supplemental/Courier New.ttf'

def font(size):
    return ImageFont.truetype(FONT, size * SCALE)

def render(frame, count=72):
    phase = frame / count * math.tau
    yaw = -.34 + .14 * math.sin(phase)
    bob = .035 * math.sin(phase)
    co, si = math.cos(yaw), math.sin(yaw)
    faces = []
    def transform(p):
        x,y,z=p
        y += bob
        xx, zz = co*x + si*z, -si*x + co*z
        return xx, -.94*y + .342*zz, .342*y + .94*zz
    def project(p):
        x,y,_=transform(p)
        return ((W/2+x*92)*SCALE,(367+y*92)*SCALE)
    def plane(points, color):
        faces.append((sum(transform(p)[2] for p in points)/len(points),points,color))
    def box(x0,y0,z0,x1,y1,z1,front,top,side):
        plane([(x0,y0,z0),(x1,y0,z0),(x1,y1,z0),(x0,y1,z0)],side)
        plane([(x0,y0,z1),(x1,y0,z1),(x1,y1,z1),(x0,y1,z1)],front)
        plane([(x0,y0,z0),(x0,y0,z1),(x0,y1,z1),(x0,y1,z0)],side)
        plane([(x1,y0,z0),(x1,y0,z1),(x1,y1,z1),(x1,y1,z0)],side)
        plane([(x0,y1,z0),(x1,y1,z0),(x1,y1,z1),(x0,y1,z1)],top)
        plane([(x0,y0,z0),(x1,y0,z0),(x1,y0,z1),(x0,y0,z1)],side)
    def panel(x0,y0,x1,y1,z,color):
        faces.append((10 + z, [(x0,y0,z),(x1,y0,z),(x1,y1,z),(x0,y1,z)],color))

    im=Image.new('RGB',(W*SCALE,H*SCALE),BG)
    d=ImageDraw.Draw(im)
    # Quiet drafting grid and contact shadow.
    for k in range(-8,9):
        d.line([project((k*.6,-.15,-2.5)),project((k*.6,-.15,3))],fill='#242316',width=1)
        d.line([project((-4.8,-.15,k*.6)),project((4.8,-.15,k*.6))],fill='#242316',width=1)
    shadow=Image.new('RGBA',im.size,(0,0,0,0))
    sd=ImageDraw.Draw(shadow)
    sd.ellipse((178*SCALE,331*SCALE,578*SCALE,456*SCALE),fill=(0,0,0,160))
    im=Image.alpha_composite(im.convert('RGBA'),shadow.filter(ImageFilter.GaussianBlur(16*SCALE))).convert('RGB')
    d=ImageDraw.Draw(im)
    # Plinth, neck, chunky CRT housing.
    box(-1.12,.0,-.52,1.12,.2,.72,'#b3a878','#e2d7ae','#8d8055')
    box(-.47,.2,-.32,.47,.72,.31,'#b9ad80','#eee3bc','#8d8055')
    box(-1.58,.7,-.8,1.58,3.08,.68,'#e2d6ac','#fff0c7','#a99b70')
    # Front bezel layers and screen.
    panel(-1.37,1.13,1.37,2.88,.686,'#8b8058')
    panel(-1.29,1.21,1.29,2.8,.695,'#2e3020')
    panel(-1.23,1.27,1.23,2.74,.704,'#101c16')
    # Phosphor scan lines.
    for k in range(28):
        yy=1.30+k*.05
        panel(-1.20,yy,1.20,yy+.007,.708,'#1d2b1c')
    # Pixel code lines, varying line lengths and subtle cursor pulse.
    panel(-1.08,2.51,-.98,2.57,.718,'#f7df1e')
    panel(-.90,2.51,-.30,2.56,.718,'#f7df1e')
    rows=[(-.95,2.31,[.24,.55,.31]),(-.82,2.13,[.46,.26,.38]),(-.82,1.95,[.22,.70]),(-.95,1.77,[.30,.42]),(-1.06,1.49,[.58])]
    for rid,(xx,yy,lengths) in enumerate(rows):
        for j,length in enumerate(lengths):
            panel(xx,yy,xx+length,yy+.035,.72,['#a4b77b','#ecd469','#788963'][(rid+j)%3])
            xx+=length+.10
    if frame%36<24:
        panel(-.36,1.48,-.26,1.55,.73,'#f7df1e')
    # Power button and disk slot.
    panel(-1.23,.86,-.59,.91,.71,'#746b49')
    panel(.97,.85,1.11,.98,.71,'#f7df1e')
    for k in range(4):
        panel(.14+k*.14,.85,.22+k*.14,.94,.71,'#9b9068')
    # Keyboard with individually modelled keycaps.
    box(-1.74,.01,.98,1.74,.20,2.1,'#a99b70','#daceaa','#82734c')
    for row in range(4):
        for col in range(12):
            x=-1.58+col*.264; z=1.12+row*.224
            accent=(row==0 and col==0) or (col==11 and row in (1,2))
            top='#f7df1e' if accent else '#f1e6bd'
            box(x,.20,z,x+.213,.28,z+.165,'#b6a77a',top,'#96895f')
    box(-.78,.205,1.98,.79,.29,2.12,'#bcad75','#f7df1e','#a68f30')
    for _,points,color in sorted(faces,key=lambda f:f[0]):
        d.polygon([project(p) for p in points],fill=color)
    # Editorial frame, retained at a legible size in README.
    d.rounded_rectangle((18*SCALE,18*SCALE,742*SCALE,542*SCALE),radius=10*SCALE,outline='#514b2d',width=SCALE)
    d.text((38*SCALE,34*SCALE),'TM / THE BUILD STATION',font=font(13),fill='#f7df1e')
    d.text((721*SCALE,34*SCALE),'EST. 2018',anchor='ra',font=font(12),fill='#b0aa91')
    d.line((38*SCALE,479*SCALE,722*SCALE,479*SCALE),fill='#514b2d',width=SCALE)
    d.text((38*SCALE,500*SCALE),'CODE. SHIP. REPEAT.',font=font(16),fill='#f7f1d5')
    d.rectangle((589*SCALE,504*SCALE,595*SCALE,510*SCALE),fill='#f7df1e')
    d.text((608*SCALE,500*SCALE),'BUILD MODE',font=font(13),fill='#f7df1e')
    return im.resize((W,H),Image.Resampling.LANCZOS)

if __name__=='__main__':
    frames=[render(i) for i in range(72)]
    # One shared palette avoids palette flicker across frames.
    sheet=Image.new('RGB',(W*3,H))
    for n,k in enumerate((0,18,54)):sheet.paste(frames[k],(n*W,0))
    palette=sheet.quantize(colors=128)
    frames=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
    out=ROOT/'assets'/'retro-computer.gif'
    frames[0].save(out,save_all=True,append_images=frames[1:],duration=80,loop=0,optimize=True,disposal=1)
    render(0).save(ROOT/'preview'/'retro-computer.png')
    print(f'{out.name}: {out.stat().st_size:,} bytes; 72 frames; 5.76 second loop')

"""Replace the header's right terminal card with the retro computer animation."""
from pathlib import Path
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from PIL import Image, ImageSequence
ROOT=Path(__file__).resolve().parents[1]
ET.register_namespace('', 'http://www.w3.org/2000/svg')
r=ET.parse(ROOT/'assets/terminal-header.svg').getroot()
for node in list(r):
    x=float(node.get('x','-1')); y=float(node.get('y','-1'))
    if x>=760 and 110<=y<=458:
        r.remove(node)
for node in r:
    if node.tag.endswith('title'):
        node.text='Terry Minn — software engineer and product builder with an animated retro computer'
with tempfile.TemporaryDirectory() as tmp:
    src=Path(tmp)/'base.svg'; base=Path(tmp)/'base.png'
    ET.ElementTree(r).write(src,encoding='unicode')
    subprocess.run(['rsvg-convert','-o',str(base),str(src)],check=True)
    background=Image.open(base).convert('RGB')
frames=[]
animation=Image.open(ROOT/'assets/retro-computer.gif')
for frame in ImageSequence.Iterator(animation):
    canvas=background.copy()
    inset=frame.convert('RGB').resize((500,368),Image.Resampling.LANCZOS)
    canvas.paste(inset,(680,99))
    frames.append(canvas)
sheet=Image.new('RGB',(1200*3,600))
for i,j in enumerate((0,18,54)):sheet.paste(frames[j],(i*1200,0))
palette=sheet.quantize(colors=192)
indexed=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
out=ROOT/'assets/animated-header.gif'
indexed[0].save(out,save_all=True,append_images=indexed[1:],duration=80,loop=0,disposal=1,optimize=True)
frames[0].save(ROOT/'preview/animated-header.png')
print(f'{out.name}: {len(frames)} frames; {out.stat().st_size:,} bytes')

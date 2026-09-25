# Profile review & publishing guide

Reviewed on 25 September 2026. This is a profile presentation review, not a source-code audit.

## What the profile should communicate

Your strongest positioning is a senior software engineer who builds products and operates their infrastructure, now working independently on Rangorithm. The supplied profile screenshot leads with a motivational quote and pinned repositories; it does not communicate your senior experience, international remote work, or operational responsibility.

The new README leads with those strengths, uses a pixel wordmark, JavaScript-yellow (#F7DF1E) and warm gold accents, emoji navigation, status badges, and a retro developer dashboard, and keeps important information as accessible Markdown. The header, badges, skill bars, and footer are local SVGs, so it does not rely on a third-party badge or statistics service.

## Suggested profile fields

**Name:** Terry Minn

**Bio:** Software engineer & indie hacker. JavaScript / TypeScript / Go. Building Rangorithm. Shipping web, mobile & backend systems; running the infra.

**Company:** Rangorithm

**Website:** https://www.facebook.com/rangorithm/

Keep your location accurate. The supplied screenshot currently says Bangkok, Thailand.

## Recommended pin order

1. **Ranger** — puts developer tooling first. Add an example workflow, a small architecture diagram, and a clear explanation of what the builder generates.
2. **Focus** — shows desktop product work. Its README describes the Pomodoro workflow and provides a download link. Make supported builds, installation, and a screenshot easy to find.
3. **3D Commerce** — shows mobile and interactive UI work. The README already includes a demo. Explain your 3D integration choices and any measured performance results.
4. **Vtoken** — shows library work. Its current README lists installation and features but would benefit from a runnable usage example, API documentation, and a clear intended-use/security scope.

For the remaining slots, use a Go backend and a public product case study when available. Do not invent repositories to fill six slots. A case study can explain the problem, your role, architecture, deployment, and results without publishing proprietary source code.

## Evidence and wording

- Your career dates, senior roles, remote work countries, language proficiency, shipped products, and current Rangorithm focus come from your message.
- [Focus](https://github.com/TerryMinn/focus), [3D Commerce](https://github.com/TerryMinn/threed-ecommerce-react-native), and [Vtoken](https://github.com/TerryMinn/vtoken) were readable publicly. Their README content informed the descriptions. Runtime behavior and code quality were not tested.
- Ranger's description and language come from your supplied GitHub screenshot; its page could not be retrieved during this review.
- The App Store Connect screenshot shows Dahlia Marketplace as **Ready for Distribution**. It shows Shwe Nyar Myay as **Rejected** and the other listed apps as **Prepare for Submission**. The public README therefore does not call every listed app released or App Store live.
- The Coolify screenshot supports the project categories and self-hosting context. A project listed in that dashboard alone does not establish uptime, production traffic, or release status.
- Your profile contact email is devwithterry@gmail.com, as explicitly supplied in your follow-up request.
- The full profile was rate-limited, the public GitHub API returned a rate-limit response, and the Rangorithm Facebook page could not be fetched. No company history, client names, revenue, user counts, or performance claims were inferred from inaccessible pages.

## Publish the profile

GitHub shows a profile README from a **public repository matching your username**, with a nonempty `README.md` in the root. See [GitHub's profile README guide](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme).

1. Open or create the public repository `TerryMinn/TerryMinn`. If it already exists, keep its existing files and merge these changes deliberately.
2. Upload this workspace's `README.md` and the complete `assets` folder to that repository's root, preserving the folder structure.
3. Commit the files and open your profile to inspect the result.
4. Apply the suggested bio and pin order using Edit profile and Customize your pins.

Upload `README.md` and every SVG in `assets/` for the public profile. Skill bars are qualitative, self-assessed categories, not measured proficiency percentages. The status badges are static editorial labels, not live service-health monitors. This review is a local handoff document.

No remote changes were made. The local workspace has no Git remote, and the GitHub CLI authentication check failed in this environment.

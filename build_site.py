#!/usr/bin/env python3
"""Build the Justin Moore / Creator Wizard swipe site.

Run: python3 build_site.py
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/JUSTIN_MOORE_Swipe")

CONFIG = {
    "SITE": "Justin Moore — Creator Wizard / Sponsor Magnet",
    "CREATOR": "Justin Moore",
    "FUNNEL_IDS": ["F132"],
    "CAPTURED": "11 August 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/JUSTIN_MOORE_Swipe",
    "BLURB": "The structural opposite of every funnel in this file. No paid traffic, no webinar, "
             "no VSL, no countdown theatre. A 27,000-person newsletter that delivers real "
             "sponsorship opportunities twice a week feeds a $27 four-day live challenge, which "
             "feeds a <b>$12,000</b> coaching program sold by a two-branch application that gates "
             "on revenue already earned. The move worth studying: he <b>killed his $3,000 course "
             "and made it a free bonus inside the coaching</b>, leaving the full sales page live "
             "as a value stack.",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Analysis"),
        ("pages.html", "Funnel pages"),
        ("copybank.html", "Copy bank"),
        ("board.html", "Wired board"),
    ],

    "STATS": [
        ("Front-end", "$27"),
        ("Back-end", "$12,000"),
        ("Newsletter", "26,998"),
        ("Funnel pages", "15"),
        ("Active Meta ads", "0"),
        ("Application Qs", "15"),
        ("App branches", "2"),
        ("Bonus stack", "$590"),
    ],

    "OFFER": [
        ("Operator", "Justin Moore &mdash; sponsorship coach, author of <i>Sponsor Magnet</i>. "
                     "Claims $5M+ personal sponsorship revenue since 2009 and 1,000+ brand "
                     "campaigns facilitated through a 7-year ad agency."),
        ("Who he sells to", "Creators, newsletter operators and podcasters who already get "
                            "inbound brand interest but convert it into $200&ndash;$1,000 deals "
                            "instead of $10,000 ones. <b>Not beginners.</b>"),
        ("Positioning", "&ldquo;We&rsquo;re coaches, not managers. You keep 100% of your "
                        "sponsorship revenue.&rdquo; The <b>0% Cut Policy</b> sits in the top nav "
                        "and the footer of every page. His named competitor is a talent manager "
                        "taking 20%, not another course."),
        ("Free tier", "Newsletter (26,998, Mon + Thu) &middot; podcast &middot; YouTube &middot; "
                      "free AI social audit tool at audit.sponsormagnet.com"),
        ("$19 tier", "<i>Sponsor Magnet</i> &mdash; $9 ebook / $10 audiobook. Also given away free "
                     "as Bonus #1 on the $27 challenge."),
        ("$27 tier", "<b>$10K Brand Deal Challenge</b>, Aug 17&ndash;20 2026, 4 days &times; 60 "
                     "mins, 11am CST. List price $97, discounted to $27 by a SUMMERSALE coupon "
                     "pre-applied in the checkout link."),
        ("Challenge stack", "$590 of bonuses on a $27 ticket &mdash; Sponsor Magnet book bundle "
                            "($19), Negotiation Scripts &amp; Templates Vault ($197), Sponsorship "
                            "Wheel Tracker ($247), Professional Brand Partnership Toolkit ($127)"),
        ("Challenge guarantee", "100% money-back within 7 days, <b>conditional on attending all "
                                "four live sessions with your camera on</b>. Re-enrol-and-refund "
                                "is explicitly barred."),
        ("$697-997 tier", "<b>Sponsor Games 2027</b> &mdash; 3-day in-person event. $997, "
                                "early bird $697. $5,000 cash grand prize plus 7 runner-up prizes "
                                "of real $2,500 brand deals funded by Lulu, Paperform and Kit."),
        ("$12,000 tier", "<b>Wizard&rsquo;s Guild</b> sponsorship coaching. Private 1-1 space, "
                         "2&times; monthly live group sessions, async support answered Tuesday and "
                         "Thursday. Monthly payment plan on a 1-year commitment. Full Brand Deal "
                         "Wizard course included free."),
        ("Coaching guarantee", "<b>None stated anywhere.</b>"),
        ("Killed offer", "<b>Brand Deal Wizard</b>, previously $3,000 (or 3&times;$1,095) as a "
                         "cohort course. The sales page is still live and opens with "
                         "&ldquo;UPDATE: Access to Brand Deal Wizard is now FREE when you join our "
                         "Sponsorship Coaching program!&rdquo;"),
        ("How the price is disclosed", "Never on a sales page. It appears once, mid-application, "
                                       "as a commitment question: &ldquo;would it be well worth "
                                       "the <b>$12k</b> investment to work with us?&rdquo;"),
        ("Affiliate economics", "Coaching 15% ongoing &middot; book 25% &middot; challenge "
                                "<b>100%</b> of the registration fee plus 15% recurring on any "
                                "coaching enrolment it produces."),
        ("Stack", "Framer (site) &middot; Kit form 6540565 (newsletter) &middot; Paperform "
                  "ztbjvcrc (application) &middot; Spiffy (checkout) &middot; Vimeo (video) "
                  "&middot; Meta Pixel + GTM + GA + <b>Hyros</b>"),
    ],

    "FINDINGS": [
        ("He killed a $3,000 course to make his $12,000 offer heavier",
         "Brand Deal Wizard used to be a $3,000 cohort course &mdash; his main product for years. "
         "The page is still live, still 27,000 characters, still 20+ Vimeo modules and 506 "
         "testimonials, and now its <b>only outbound link is the coaching application</b>. The "
         "first line of the page is &ldquo;UPDATE: Access to Brand Deal Wizard is now FREE when "
         "you join our Sponsorship Coaching program!&rdquo; He didn't delete the asset, he "
         "demoted it into the value stack of the offer above it. The whole sales page now works "
         "as proof of what the $12k includes."),
        ("The $27 ticket is a buyer filter, not a revenue line",
         "$27 against $590 of stacked bonuses cannot be about margin. It does three things a free "
         "webinar can&rsquo;t: it takes a card, it takes a <b>phone number plus explicit SMS "
         "autodialer consent</b>, and it makes the refund conditional on showing up to all four "
         "days with camera on. He is buying a list of people who have paid him once and can "
         "legally be called. <i>This is a read, not his stated intent.</i>"),
        ("The refund condition IS the show-rate mechanism",
         "&ldquo;If you attend all the live sessions (with your camera on!), pay attention, put in "
         "the work, and don&rsquo;t feel like you received a massive amount of value&hellip; full "
         "refund within 7 days.&rdquo; The guarantee is only claimable by someone who attended "
         "everything. Nobody has to be nagged into showing up &mdash; the money does it. Replays "
         "also expire when the next day starts. Compare: we currently run a free class and fight "
         "for show rate with follow-up volume."),
        ("The lead magnet is a recurring deliverable, not a PDF",
         "&ldquo;Get brand sponsorship opportunities in your inbox every Monday and Thursday.&rdquo; "
         "The subscriber has a reason to open twice a week forever, and the proof on the opt-in "
         "page puts a number on the free thing: <b>&ldquo;I have made over $17,000 from brand "
         "deals I found through Justin&rsquo;s newsletter.&rdquo;</b> A PDF is consumed once. This "
         "compounds, and it is why 27,000 people is enough traffic to run the whole business."),
        ("The application is two branches and gates on cash already earned",
         "Paperform ztbjvcrc, titled <b>&ldquo;Sponsorship Coaching Application (Organic)&rdquo;</b> "
         "&mdash; the word <i>Organic</i> means a paid-traffic version exists. Branch A opens "
         "&ldquo;Have you negotiated a sponsorship in the last 30 days?&rdquo; then asks deals "
         "closed in 12 months, sponsorship revenue AND total revenue in six bands from $0 to "
         "$200k+, largest deal ever, monthly inbound inquiries, audience size, and job situation. "
         "Branch B, for people who haven&rsquo;t closed recently, swaps in the question A never "
         "gets: <b>&ldquo;Have you invested money into growing your business in the last 12 "
         "months? (coaching, courses, etc.)&rdquo;</b> If you can&rsquo;t show revenue, he checks "
         "whether you have ever paid for help."),
        ("The price is a commitment question, not a disclosure",
         "&ldquo;If we could help you achieve your sponsorship goals and be in your corner with "
         "your pitches, pricing, negotiations, packages, and proposals, <b>would it be well worth "
         "the $12k investment to work with us?</b>&rdquo; &mdash; Yes / No / Maybe. Immediately "
         "followed by &ldquo;how soon would you want to get started? ASAP / 1&ndash;2 months / 3+ "
         "months / I&rsquo;m not interested in coaching at all.&rdquo; Price objection and timeline "
         "objection are both dead in writing before a human dials."),
        ("Zero paid traffic. The audience IS the acquisition channel.",
         "Meta Pixel, GTM, GA and Hyros are all installed on the challenge page &mdash; he is "
         "instrumented to run paid &mdash; but an ad-library sweep returned <b>no active Creator "
         "Wizard ads</b>. Traffic is the newsletter, the podcast, the YouTube channel, a published "
         "book, an affiliate program paying 100% on the front end, and borrowed authority from Ali "
         "Abdaal and Jay Clouse. <i>Keyword search of the ad library is not exhaustive; treat as "
         "evidence, not proof.</i>"),
        ("Proof is named people with public identities, never screenshots",
         "Ali Abdaal (&pound;200,000, ~2&times; sponsorship revenue), Jenny Hoyos ($15,000, with a "
         "full case-study page), Jenny Wood ($6,000 first deal off one email), Molly Donlan "
         "($17,000 from newsletter opportunities). <b>Zero income screenshots anywhere.</b> Every "
         "claim is attached to a person you can go verify yourself, which is a harder asset to "
         "build and an unfalsifiable one to attack."),
        ("The event's prize is the product",
         "Sponsor Games 2027 gives away $5,000 cash plus <b>seven real $2,500 brand deals</b> "
         "&mdash; funded by Lulu, Paperform and Kit. Attendees at a sponsorship event win actual "
         "sponsorships. The event proves the mechanism, and his sponsors pay the $17,500 prize "
         "pool. Tickets are on sale roughly 18 months out."),
        ("Day 3 of the challenge is unfakeable proof of mechanism",
         "&ldquo;We&rsquo;ll select creators LIVE to share their dream brands, then I&rsquo;ll show "
         "you exactly how to stalk those brands on social media to uncover the hidden clues that "
         "reveal what should be in your $10K package. You&rsquo;ll watch me decode their marketing "
         "strategy in real-time.&rdquo; Live diagnosis on a stranger&rsquo;s real situation cannot "
         "be scripted, and it is the day nobody wants to catch on replay."),
    ],

    "FUNNEL": [
        ("Traffic &mdash; 100% owned", "newsletter &middot; podcast &middot; YouTube &middot; book &middot; affiliates",
         "26,998 newsletter subscribers mailed Monday and Thursday with real sponsorship "
         "opportunities. Plus a weekly podcast, a YouTube channel, a published book, and an "
         "affiliate program paying <b>100%</b> of the challenge fee. "
         '<span class="tag bad">no active Meta ads found</span>'),
        ("Hub", "creatorwizard.com",
         "Not a sales page &mdash; a content hub. Podcast, articles, case studies and four offers "
         "in the nav. Hero CTA is the positioning: &ldquo;See How You Keep 100%&rdquo;."),
        ("Self-select router", "creatorwizard.com/how-we-can-help",
         "A footer link on every page reading &ldquo;I don&rsquo;t know what I need&rdquo;. Routes "
         "to newsletter / podcast / book / coaching by intent. Catches the visitor who isn&rsquo;t "
         "ready to buy instead of letting them bounce."),
        ("Newsletter opt-in", "pages.creatorwizard.com/join",
         "First name + email only. No phone, no qualification, no friction. Kit form 6540565. "
         "CTA is <b>&ldquo;Send Me Sponsorships&rdquo;</b> &mdash; not &ldquo;subscribe&rdquo;."),
        ("Free AI audit tool", "audit.sponsormagnet.com",
         "Enter a YouTube / TikTok / IG handle, get a personalised report on why sponsors "
         "aren&rsquo;t buying you. A tool, not a PDF &mdash; the output is a diagnosis, so the "
         "follow-up already knows the prospect&rsquo;s specific gap."),
        ("Book", "sponsormagnet.com",
         "$9 ebook / $10 audiobook. The authority asset the whole ladder leans on, and "
         "simultaneously Bonus #1 on the $27 challenge."),
        ("Front-end offer", "creatorwizard.com/challenge",
         "<b>$10K Brand Deal Challenge</b>, Aug 17&ndash;20 2026. &ldquo;Let&rsquo;s build your "
         "$10K+ Brand Deal Offer in Just 4 Days&rdquo; with the objection pre-handled in the "
         "subhead: &ldquo;even if you don&rsquo;t have a massive audience&hellip; or you&rsquo;re "
         "in a weird niche&rdquo;. Meta Pixel + GTM + GA + Hyros all fire here."),
        ("Checkout", "creatorwizard.spiffy.co/checkout/10kchallenge?c=SUMMERSALE",
         "$97 struck to <b>$27</b> by a coupon pre-applied in the link, so the buyer never types a "
         "code and never sees full price. Five-day countdown. "
         '<span class="tag bad">phone number + SMS autodialer consent collected on a $27 order</span>'),
        ("The 4 days", "live, 11am CST",
         "Day 1 Command $10K With Confidence &middot; Day 2 $10K Package Structures &middot; Day 3 "
         "Use Social Clues to Build the Package (creators picked LIVE) &middot; Day 4 Scale to "
         "Multiple 5&ndash;6 Figures/yr. Replays expire when the next day starts."),
        ("The demoted course", "branddealwizard.com",
         "Was $3,000. Now free inside the coaching. Full sales page still live; its only outbound "
         "link is the coaching."),
        ("Application", "ztbjvcrc.paperform.co",
         "Paperform titled &ldquo;Sponsorship Coaching Application <b>(Organic)</b>&rdquo;. Two "
         "branches, 15 questions, revenue in six bands, and the $12k commitment question. Never "
         "submitted."),
        ("Back end", "wizardsguild.com",
         "<b>Wizard&rsquo;s Guild &mdash; $12,000.</b> Private 1-1 plus 2&times; monthly group "
         "live, async answered Tue + Thu, monthly plan on a 1-year commitment. No guarantee "
         "stated. wizardsguild.com and creatorwizard.com/coaching both 301 straight to the "
         "application &mdash; there is no live price page."),
        ("Live event", "sponsorgames.com",
         "Sponsor Games 2027. $997, early bird $697. $5,000 cash grand prize plus seven $2,500 "
         "brand deals funded by Lulu, Paperform and Kit."),
    ],

    "TRANSCRIPT_GROUPS": [],
    "SLIDE_PAGES": [],
    "VIDEOS": [],

    "ANALYSIS": """
<div class="note warn"><b>Read this first.</b> This is not a webinar funnel and there is nothing
to transcribe. There is no VSL, no evergreen class, no replay page and no recorded pitch &mdash;
the only video assets are short Framer background loops and Vimeo course modules behind the paid
wall. The <b>$10K Brand Deal Challenge runs live Aug 17&ndash;20 2026</b>, so the pitch does not
exist yet. Everything below is read off 15 captured pages, a live checkout, and the raw config of
the live application form.</div>

<h2 class="sec">Why this one is in the file</h2>
<p>Every other funnel we have swiped is the same machine as ours: paid traffic, a free class,
a countdown, an application, a closer. Justin Moore runs the opposite machine and appears to
make it work &mdash; $5M+ in personal sponsorship revenue, a published book, Ali Abdaal as a
public client, and a $12,000 program with no ad spend behind it.</p>
<p>He is not a direct competitor. He sells to creators who already get inbound brand interest;
we sell to people trying to become creators. But he is selling <i>into the same room</i>, and
three of his mechanics attack problems we actually have.</p>

<h2 class="sec">The ladder</h2>
<div class="tablewrap"><table>
<tr><th>Rung</th><th>Price</th><th>Job it does</th></tr>
<tr><td>Newsletter</td><td>free</td><td>Delivers real sponsorship opportunities twice a week. The proof line has a dollar figure on it.</td></tr>
<tr><td>AI audit tool</td><td>free</td><td>Diagnoses the prospect, so the follow-up knows their specific gap</td></tr>
<tr><td>Podcast + YouTube</td><td>free</td><td>Authority, and the top of the affiliate/borrowed-audience layer</td></tr>
<tr><td><i>Sponsor Magnet</i></td><td>$9&ndash;19</td><td>Authority asset. Doubles as Bonus #1 on the challenge.</td></tr>
<tr><td><b>$10K Brand Deal Challenge</b></td><td><b>$27</b> (list $97)</td><td><b>Buyer filter.</b> Takes a card, a phone number and SMS consent.</td></tr>
<tr><td>Sponsor Games</td><td>$697&ndash;997</td><td>In-person room. Prize pool funded by his own sponsors.</td></tr>
<tr><td>Brand Deal Wizard</td><td><s>$3,000</s> free</td><td>Demoted. Now the value stack inside the coaching.</td></tr>
<tr><td><b>Wizard&rsquo;s Guild</b></td><td><b>$12,000</b></td><td>The business. Sold by two-branch application, price disclosed inside it.</td></tr>
</table></div>

<h2 class="sec">Worth taking</h2>
<div class="grid g2">
<div class="card"><h3>Make the guarantee conditional on attendance</h3>
<p>&ldquo;Full refund &mdash; if you attend all the live sessions <b>with your camera on</b>.&rdquo;
The refund is only claimable by someone who showed up to everything. Show rate is our number-one
bottleneck and we currently attack it with follow-up volume. He attacks it with the terms of the
offer, and it costs nothing to run.</p></div>
<div class="card"><h3>Charge $27 instead of charging nothing</h3>
<p>A paid front end buys a card on file, a phone number, and legal SMS consent &mdash; then the
$590 bonus stack makes the $27 feel like theft. Our free class gives us none of those three. A
$27&ndash;47 paid front end would filter the tyre-kickers our setters currently burn hours on and
give us a callable list of proven buyers.</p></div>
<div class="card"><h3>Put the price in the application as a commitment question</h3>
<p>&ldquo;Would it be well worth the $12k investment to work with us? Yes / No / Maybe&rdquo;,
followed by &ldquo;how soon would you want to get started?&rdquo; The prospect types the price and
the timeline before a closer ever dials. Both objections are pre-handled in writing, and the
No/Maybe answers are a free routing signal.</p></div>
<div class="card"><h3>Branch the application on proof of money</h3>
<p>If they have closed deals recently he asks for revenue bands. If they haven&rsquo;t, he asks
&ldquo;have you invested money into growing your business in the last 12 months?&rdquo; Two
different definitions of qualified, one form. Our lead grader already weights proven-earner and
ability-to-pay heaviest &mdash; this is the same logic expressed as branching form
logic instead of a scoring rubric.</p></div>
<div class="card"><h3>Make the lead magnet a recurring deliverable</h3>
<p>Not a PDF. An actual list of sponsorship opportunities, twice a week, forever. It is the reason
27,000 subscribers is enough traffic to carry a business with no ad spend. Our equivalent would
be a recurring feed of live brand briefs the audience genuinely can&rsquo;t get elsewhere.</p></div>
<div class="card"><h3>Give a live diagnosis on a real stranger</h3>
<p>Day 3 picks creators live, takes their dream brand, and decodes that brand&rsquo;s social in real
time. It cannot be scripted, it proves the mechanism better than any testimonial, and it makes
that day unskippable.</p></div>
<div class="card"><h3>Name the enemy in the nav</h3>
<p>&ldquo;0% Cut Policy &mdash; we&rsquo;re coaches, not managers.&rdquo; Top nav and footer of
every page. He is not arguing against another course, he is arguing against a talent manager
taking 20%. One line, on every page, and every visitor knows what he is instead of what he
does.</p></div>
<div class="card"><h3>Let the prize be the product</h3>
<p>Seven attendees at Sponsor Games win real $2,500 brand deals, funded by his own sponsors. The
event demonstrates the mechanism and someone else pays for the demonstration.</p></div>
</div>

<h2 class="sec">Not worth taking</h2>
<p><b>The no-ads model is not portable to us.</b> He spent 15 years building the audience that
feeds this, and the book plus the Ali Abdaal relationship are not assets you can buy this quarter.
Reading &ldquo;he runs no ads&rdquo; as a strategy would be the wrong lesson &mdash; the lesson is
what a paid front end does for a list, and that works with paid traffic too.</p>
<p><b>No guarantee on the $12k.</b> He can get away with that because the book, the podcast and
the named clients have already done the trust work. We cannot, and our objection set is different
&mdash; portfolio-perfectionism and burned-by-a-past-coach both need a guarantee to answer them.</p>
<p><b>The price-hidden coaching page.</b> wizardsguild.com and creatorwizard.com/coaching both 301
straight to the application form, so a warm visitor who wants to evaluate the offer has nowhere to
land. That is a leak, not a technique.</p>

<h2 class="sec">Open questions &mdash; not captured</h2>
<ul>
<li><b>What happens between the $27 buy and the application.</b> The challenge doesn&rsquo;t start
until Aug 17 and the checkout requires a card and a phone number, so under the swipe hard rules we
never submitted. No post-purchase sequence, no order bump, no upsell path, and no evidence of how
Day 4 pitches into the coaching.</li>
<li><b>The paid-traffic application.</b> The live form is titled &ldquo;(Organic)&rdquo;, which
means a second version exists for paid traffic. We have not found it, and its existence is the
strongest single hint that he does run ads somewhere we haven&rsquo;t looked.</li>
<li><b>Whether $12,000 is the only price.</b> The application says $12k and the affiliates page
says &ldquo;5 figures&rdquo;. A 2024 third-party write-up described $297/mo group and $1k/mo
private tiers &mdash; almost certainly retired, but there is no current price page to check
against.</li>
<li><b>Email sequences.</b> Not yet in the inbox. Registering the research identity for the
newsletter would surface his welcome flow and the challenge promo sequence &mdash; a one-line
opt-in with no phone field, so it is safe to run if Will wants it.</li>
</ul>
""",
}

build(CONFIG)

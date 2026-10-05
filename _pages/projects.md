---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
hide_archive_title: true
excerpt: "Projects on collaboration among intelligent entities, with their papers and project pages."
---

<div class="research-page projects-page">
  <p class="projects-scholar">Full list on <a href="https://scholar.google.com/citations?hl=en&amp;user=HnhN3tYAAAAJ">Google Scholar</a></p>

  <section class="research-year-group" aria-labelledby="year-2026">
    <h2 id="year-2026" class="research-divider">2026</h2>

    <div class="research-work-list">
      <article id="work-tea" class="research-work">
        <div class="research-work-copy">
          <h3>TEA: Structurally Representing Arbitrary LLM Agents Collaboration</h3>
          <p class="research-work-authors"><strong>H. Yang</strong>, Y. Mao, Z. Zhang, Y. Yao, J. Chen, T. Lan, and C. Joe-Wong</p>
          <div class="research-work-more">
            <span class="research-work-venue">Preprint 2026</span>
            <span class="research-work-inline-links">
              <button type="button" class="research-work-toggle" aria-expanded="false" aria-controls="overview-1">Overview</button>
              <a href="/tea/">Webpage</a>
            </span>
            <p class="research-work-overview" id="overview-1">Introduces Task-Environment-Agents (TEA), a structural representation that couples an Agent Interaction Graph with a Task Activity Graph and the shared environment. It makes evolving collaboration explicit without prescribing agent reasoning, behavior, or communication order, and Infuse uses TEA records to recover, assess, and improve collaboration policies.</p>
          </div>
        </div>
        <figure class="research-work-figure">
          <a href="/tea/figs/overview.png" aria-label="Open the full figure"><img src="/tea/figs/overview.png" alt="TEA overview: a collaboration policy is executed, recorded as task, environment, and agent views, recovered into a topology and rules, and infused into an updated policy." loading="lazy"></a>
        </figure>
      </article>

      <article id="work-icore" class="research-work research-work--icore">
        <div class="research-work-copy">
          <h3>Auditing Emergent LLM-Agent Collaboration through Cooperation-Obligation Coupling</h3>
          <p class="research-work-authors">Z. Zhang*, <strong>H. Yang*</strong>, C. Joe-Wong, and T. Lan</p>
          <div class="research-work-more">
            <span class="research-work-venue">Preprint 2026</span>
            <span class="research-work-inline-links">
              <button type="button" class="research-work-toggle" aria-expanded="false" aria-controls="overview-2">Overview</button>
              <a href="https://arxiv.org/abs/2607.27429">Paper</a>
            </span>
            <p class="research-work-overview" id="overview-2">Represents emergent collaboration through coupled cooperation-obligation graphs that formalize work soundness and assignment stability. Their joint satisfaction quantifies state quality and yields a conditional performance bound.</p>
          </div>
        </div>
        <figure class="research-work-figure research-work-figure--icore" aria-label="iCORE: G is interaction, Q is obligation, and Pi is the evidence-backed coupling between them">
          <div class="icore-mini" aria-hidden="true">
            <i class="icore-mini-symbol icore-mini-symbol--g">G</i>
            <div class="icore-mini-chain icore-mini-chain--g">
              <span>action</span><span>artifact</span><span>evidence</span>
            </div>
            <i class="icore-mini-symbol icore-mini-symbol--pi">&Pi;</i>
            <div class="icore-mini-links"><span></span><span></span><span></span></div>
            <i class="icore-mini-symbol icore-mini-symbol--q">Q</i>
            <div class="icore-mini-chain icore-mini-chain--q">
              <span>open</span><span>assigned</span><span>accepted</span>
            </div>
          </div>
        </figure>
      </article>

      <article id="work-coop2" class="research-work">
        <div class="research-work-copy">
          <h3>COOP<sup>2</sup>: Defining, Observing, and Repairing Cooperation in LLM Multi-Agent Systems</h3>
          <p class="research-work-authors"><strong>H. Yang</strong>, N. Nourzad, S. Chen, M. Siew, J. Chen, and C. Joe-Wong</p>
          <div class="research-work-more">
            <span class="research-work-venue">Preprint 2026</span>
            <span class="research-work-inline-links">
              <button type="button" class="research-work-toggle" aria-expanded="false" aria-controls="overview-3">Overview</button>
              <a href="https://arxiv.org/abs/2603.00349">Paper</a>
              <a href="/coop2/">Webpage</a>
            </span>
            <p class="research-work-overview" id="overview-3">Formalizes cooperation from two connected sides: what cooperative tasks require and how LLM agents reason, communicate, use tools, and act across cognitive and primitive layers. Aligning both makes cooperation observable, while the COOP<sup>2</sup>-Repair case study highlights how the formulation can support targeted replanning.</p>
          </div>
        </div>
        <figure class="research-work-figure">
          <a href="/coop2/figs/overview.png" aria-label="Open the full figure"><img src="/coop2/figs/overview.png" alt="COOP squared connects symbolic agent activity with grounded environment execution." loading="lazy"></a>
        </figure>
      </article>

      <article id="work-dig" class="research-work">
        <div class="research-work-copy">
          <h3>DIG to Heal: Scaling General-Purpose Agent Collaboration via Explainable Dynamic Decision Paths</h3>
          <p class="research-work-authors"><strong>H. Yang</strong>, H. Lee, Y. Yao, Z. Liu, K. Liu, J. Chen, and C. Joe-Wong</p>
          <div class="research-work-more">
            <span class="research-work-venue">Preprint 2026</span>
            <span class="research-work-inline-links">
              <button type="button" class="research-work-toggle" aria-expanded="false" aria-controls="overview-4">Overview</button>
              <a href="https://arxiv.org/abs/2603.00309">Paper</a>
              <a href="/dig/">Webpage</a>
            </span>
            <p class="research-work-overview" id="overview-4">Represents asynchronous multi-agent execution as a time-evolving graph of agent activations and events. The graph exposes reachability and progress failures and supports online healing through information injection and rerouting.</p>
          </div>
        </div>
        <figure class="research-work-figure">
          <a href="/dig/figs/fig2_new.png" aria-label="Open the full figure"><img src="/dig/figs/fig2_new.png" alt="Dynamic Interaction Graph representation of agent activations and events." loading="lazy"></a>
        </figure>
      </article>

      <article id="work-five-ws" class="research-work">
        <div class="research-work-copy">
          <h3>The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why: A Survey from MARL to Emergent Language and LLMs</h3>
          <p class="research-work-authors">J. Chen, <strong>H. Yang</strong>, Z. Liu, and C. Joe-Wong</p>
          <div class="research-work-more">
            <span class="research-work-venue"><a href="https://jmlr.org/tmlr/">TMLR 2026</a></span>
            <span class="research-work-inline-links">
              <button type="button" class="research-work-toggle" aria-expanded="false" aria-controls="overview-5">Overview</button>
              <a href="https://openreview.net/forum?id=LGsed0QQVq">Paper</a>
            </span>
            <p class="research-work-overview" id="overview-5">Surveys communication structures across MARL, emergent language, and LLM-based multi-agent systems through who talks to whom, when, what, and why. It reveals how organizational assumptions are often built into communication mechanisms rather than collaboration examined directly.</p>
          </div>
        </div>
        <figure class="research-work-figure research-work-figure--five-ws">
          <a href="/assets/images/research/five-ws-figure-11.png" aria-label="Open the full figure"><img src="/assets/images/research/five-ws-figure-11.png" alt="Figure 11 from the Five Ws survey: an overview of LLM-agent components, multi-agent communication designs, applications, and challenges." loading="lazy"></a>
        </figure>
      </article>

    </div>
  </section>

  <section class="research-year-group" aria-labelledby="year-2025">
    <h2 id="year-2025" class="research-divider">2025</h2>

    <div class="research-work-list">
      <article id="work-drwell" class="research-work">
        <div class="research-work-copy">
          <h3>DR. WELL: Dynamic Reasoning and Learning with Symbolic World Model for Embodied LLM-Based Multi-Agent Collaboration</h3>
          <p class="research-work-authors">N. Nourzad*, <strong>H. Yang*</strong>, S. Chen, and C. Joe-Wong</p>
          <div class="research-work-more">
            <span class="research-work-venue"><a href="https://sites.google.com/view/law-2025">NeurIPS 2025 LAW Workshop</a></span>
            <span class="research-work-inline-links">
              <button type="button" class="research-work-toggle" aria-expanded="false" aria-controls="overview-6">Overview</button>
              <a href="https://arxiv.org/abs/2511.04646">Paper</a>
              <a href="https://narjesno.github.io/DR.WELL/">Webpage</a>
            </span>
            <p class="research-work-overview" id="overview-6">Coordinates embodied agents through two phases: agents negotiate and commit to roles, then independently execute symbolic plans grounded in a shared world model. Working above raw trajectories makes collaboration more reusable and interpretable while allowing the world model to improve across episodes.</p>
          </div>
        </div>
        <figure class="research-work-figure research-work-figure--drwell">
          <a href="/assets/images/research/drwell-overview.png" aria-label="Open the full figure"><img src="/assets/images/research/drwell-overview.png" alt="DR. WELL overview: agents negotiate roles, execute symbolic plans, revise a shared world model, and validate plans in the environment." loading="lazy"></a>
        </figure>
      </article>

      <article id="work-cube" class="research-work">
        <div class="research-work-copy">
          <h3>CUBE: Collaborative Multi-Agent Block-Pushing Environment for Collective Planning with LLM Agents</h3>
          <p class="research-work-authors"><strong>H. Yang*</strong>, N. Nourzad*, S. Chen, and C. Joe-Wong</p>
          <div class="research-work-more">
            <span class="research-work-venue"><a href="https://sea-workshop.github.io/">NeurIPS 2025 SEA Workshop</a></span>
            <span class="research-work-inline-links">
              <button type="button" class="research-work-toggle" aria-expanded="false" aria-controls="overview-7">Overview</button>
              <a href="https://openreview.net/forum?id=T7OoS6t11c">Paper</a>
              <a href="/cube/">Webpage</a>
            </span>
            <p class="research-work-overview" id="overview-7">Designs weighted blocks, force, congestion, collisions, and timing so task-induced dependencies and collective capability become explicit. Some goals are individually infeasible, allowing collaboration to be studied as a property of the task rather than only of the policy.</p>
          </div>
        </div>
        <figure class="research-work-figure">
          <a href="/cube/static/images/embodied_constraints.png" aria-label="Open the full figure"><img src="/cube/static/images/embodied_constraints.png" alt="Physical constraints in the CUBE block-pushing environment." loading="lazy"></a>
        </figure>
      </article>

      <article id="work-damcs" class="research-work">
        <div class="research-work-copy">
          <h3>LLM-Powered Decentralized Generative Agents with Adaptive Hierarchical Knowledge Graph for Cooperative Planning</h3>
          <p class="research-work-authors"><strong>H. Yang</strong>, J. Chen, M. Siew, T. Lorido-Botran, and C. Joe-Wong</p>
          <p class="research-work-recognition"><a href="https://rdi.berkeley.edu/llm-agents-hackathon/">First Place (tie), Decentralized and Multi-Agents Track</a> &middot; Berkeley RDI LLM Agents MOOC Hackathon</p>
          <div class="research-work-more">
            <span class="research-work-venue"><a href="https://sites.google.com/view/marw-ai-agents">AAAI 2025 MARW Workshop</a></span>
            <span class="research-work-inline-links">
              <button type="button" class="research-work-toggle" aria-expanded="false" aria-controls="overview-8">Overview</button>
              <a href="https://arxiv.org/abs/2502.05453">Paper</a>
              <a href="/damcs/">Webpage</a>
            </span>
            <p class="research-work-overview" id="overview-8">Introduces DAMCS, whose adaptive hierarchical knowledge graph organizes multimodal experience into shared and local memory. Decentralized agents can reason from past interactions while sharing relevant knowledge rather than entire histories during long-horizon planning under dependency constraints.</p>
          </div>
        </div>
        <figure class="research-work-figure">
          <a href="/damcs/static/images/abstract.png" aria-label="Open the full figure"><img src="/damcs/static/images/abstract.png" alt="Agents in Multi-Agent Crafter cooperate through structured memory and communication." loading="lazy"></a>
        </figure>
      </article>

    </div>
  </section>

  <section class="research-year-group" aria-labelledby="year-2024">
    <h2 id="year-2024" class="research-divider">2024</h2>

    <div class="research-work-list">
      <article id="work-digital-twin" class="research-work">
        <div class="research-work-copy">
          <h3>An LLM-Based Digital Twin for Optimizing Human-in-the-Loop Systems</h3>
          <p class="research-work-authors"><strong>H. Yang</strong>, M. Siew, and C. Joe-Wong</p>
          <div class="research-work-more">
            <span class="research-work-venue"><a href="https://fmsys24.github.io/">IEEE FMSys 2024 Workshop</a> &middot; Co-located with <a href="https://cps-iot-week2024.ie.cuhk.edu.hk/">CPS-IoT Week</a></span>
            <span class="research-work-inline-links">
              <button type="button" class="research-work-toggle" aria-expanded="false" aria-controls="overview-9">Overview</button>
              <a href="https://arxiv.org/abs/2403.16809">Paper</a>
            </span>
            <p class="research-work-overview" id="overview-9">Uses an LLM-based digital twin to simulate heterogeneous human feedback for adaptive HVAC control. Aggregated occupant preferences enter the reward objective, making collective preference part of what the controller learns to optimize.</p>
          </div>
        </div>
        <figure class="research-work-figure">
          <a href="/assets/images/research/digital-twin-figure-1.png" aria-label="Open the full figure"><img src="/assets/images/research/digital-twin-figure-1.png" alt="Figure 1 from the digital-twin paper: simulated population dynamics and aggregated thermal preferences train an agent-in-the-loop controller for comfort and energy savings." loading="lazy"></a>
        </figure>
      </article>
    </div>
  </section>

  <section class="research-year-group research-healthcare" aria-labelledby="year-2023">
    <h2 id="year-2023" class="research-divider">2023 and before</h2>

    <header class="research-healthcare-intro">
      <p class="research-healthcare-subtitle">Machine Learning for Healthcare</p>
      <p>Before focusing on multi-agent systems, I worked closely with clinicians on decision support and scarce-resource allocation across international, national, and local datasets. These projects moved from validating risk scores, to aligning predictions with clinical decision horizons, to estimating treatment effects when a potentially beneficial intervention cannot be given to every eligible patient.</p>
    </header>

    <div class="research-work-list research-work-list--healthcare">
      <article class="research-work research-work--text">
        <div class="research-work-copy">
          <h3>Multi-Horizon Predictive Models for Guiding Extracorporeal Resource Allocation in Critically Ill COVID-19 Patients</h3>
          <p class="research-work-authors">B. Xue, N. Shah, <strong>H. Yang</strong>, T. Kannampallil, P. R. O. Payne, C. Lu, and A. S. Said</p>
          <div class="research-work-more">
            <span class="research-work-venue"><a href="https://academic.oup.com/jamia">JAMIA 2023</a></span>
            <span class="research-work-inline-links">
              <button type="button" class="research-work-toggle" aria-expanded="false" aria-controls="overview-10">Overview</button>
              <a href="https://doi.org/10.1093/jamia/ocac256">Paper</a>
            </span>
            <p class="research-work-overview" id="overview-10">Developed calibrated predictions at multiple time horizons for critically ill COVID-19 patients, aligning risk estimates with when scarce ECMO allocation decisions must be made.</p>
          </div>
        </div>
      </article>

      <article class="research-work research-work--text">
        <div class="research-work-copy">
          <h3>Assisting Clinical Decisions for Scarcely Available Treatment via Disentangled Latent Representation</h3>
          <p class="research-work-authors">B. Xue, A. S. Said, Z. Xu, H. Liu, N. Shah, <strong>H. Yang</strong>, P. R. O. Payne, and C. Lu</p>
          <div class="research-work-more">
            <span class="research-work-venue"><a href="https://kdd.org/kdd2023/">ACM SIGKDD 2023</a></span>
            <span class="research-work-inline-links">
              <button type="button" class="research-work-toggle" aria-expanded="false" aria-controls="overview-11">Overview</button>
              <a href="https://doi.org/10.1145/3580305.3599774">Paper</a>
            </span>
            <p class="research-work-overview" id="overview-11">Used disentangled latent representations to separate prognostic factors from heterogeneous treatment effects, supporting decisions when treatment capacity is limited.</p>
          </div>
        </div>
      </article>

      <article class="research-work research-work--text">
        <div class="research-work-copy">
          <h3>Validation of ECMO Mortality Prediction and Severity-of-Illness Scores in an International COVID-19 Cohort</h3>
          <p class="research-work-authors">N. Shah, B. Xue, Z. Xu, <strong>H. Yang</strong>, E. Marwali, H. Dalton, P. P. R. Payne, C. Lu, A. S. Said, and the ISARIC Clinical Characterisation Group</p>
          <div class="research-work-more">
            <span class="research-work-venue"><a href="https://onlinelibrary.wiley.com/journal/15251594">Artificial Organs 2023</a></span>
            <span class="research-work-inline-links">
              <button type="button" class="research-work-toggle" aria-expanded="false" aria-controls="overview-12">Overview</button>
              <a href="https://doi.org/10.1111/aor.14542">Paper</a>
            </span>
            <p class="research-work-overview" id="overview-12">Evaluated mortality prediction and severity-of-illness scores in an international COVID-19 cohort, testing how established tools behave across a diverse clinical population.</p>
          </div>
        </div>
      </article>
    </div>
  </section>

</div>

<dialog class="figure-lightbox" aria-label="Enlarged figure">
  <img alt="">
</dialog>

<script>
  /* Comments in this script are block comments on purpose: the live site compresses its HTML onto one
     line (compress_html in _config.yml), and a line comment would then swallow the code after it. */

  /* Overview toggles: without this script the overviews stay visible (see .js rules in _research.scss). */
  document.querySelectorAll(".research-work-toggle").forEach(function (button) {
    button.addEventListener("click", function () {
      button.setAttribute("aria-expanded", button.getAttribute("aria-expanded") === "true" ? "false" : "true");
    });
  });

  /* Figure viewer: a thumbnail opens its full figure over the page; a click anywhere or Escape closes it.
     Without this script the thumbnail is a plain link to the image. */
  (function () {
    var box = document.querySelector(".figure-lightbox");
    if (!box || typeof box.showModal !== "function") { return; }
    var full = box.querySelector("img");
    document.querySelectorAll(".research-work-figure a").forEach(function (link) {
      link.addEventListener("click", function (event) {
        event.preventDefault();
        var thumb = link.querySelector("img");
        full.src = link.getAttribute("href");
        full.alt = thumb ? thumb.alt : "";
        box.showModal();
      });
    });
    box.addEventListener("click", function () { box.close(); });
  })();
</script>

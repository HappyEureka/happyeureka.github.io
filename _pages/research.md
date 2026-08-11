---
layout: archive
title: "Collaboration among intelligent entities"
permalink: /research/
author_profile: true
hide_archive_title: true
excerpt: "Definition, representation, and computation of collaboration among intelligent entities."
---

<div class="research-page">
  <h1 class="research-program-title">Collaboration among intelligent entities</h1>
  <section class="research-intro">
    <p class="research-summary">From exploring what constitutes collaboration, to representing emergent structure, to examining what becomes computationally possible.</p>
    <p class="research-description">
      I approach collaboration through how it unfolds: agents interact, tasks evolve, interdependencies emerge, and individual contributions become collectively consequential. These questions are agnostic to entity type; my current work studies how they play out among LLM agents.
    </p>
    <p class="research-links">
      <a href="https://scholar.google.com/citations?hl=en&amp;user=HnhN3tYAAAAJ">Google Scholar</a>
    </p>
  </section>

  <section class="research-section research-directions" aria-labelledby="directions-heading">
    <h2 id="directions-heading" class="screen-reader-text">Research directions</h2>

    <figure class="research-cycle" aria-label="Definition, representation, and computation form a bidirectional cycle.">
      <div class="research-cycle-diagram">
        <span class="research-cycle-return" aria-hidden="true">
          <span class="research-cycle-return-arrow research-cycle-return-arrow--start"></span>
          <span class="research-cycle-return-arrow research-cycle-return-arrow--end"></span>
        </span>

        <div class="research-cycle-node research-cycle-node--definition">
          <h3>Definition</h3>
          <p class="research-cycle-theme">Interdependence &middot; collective capability &middot; collaborative primitives</p>
          <p class="research-cycle-question">What constitutes collaboration among intelligent entities, and which primitives distinguish it from mere group behavior?</p>
        </div>
        <span class="research-cycle-edge research-cycle-edge--one" aria-hidden="true"></span>
        <div class="research-cycle-node research-cycle-node--representation">
          <h3>Representation</h3>
          <p class="research-cycle-theme">Expressiveness &middot; generalizability &middot; scalability</p>
          <p class="research-cycle-question">What representational structure can capture emergent collaboration across tasks, teams, and scales—and under what assumptions?</p>
        </div>
        <span class="research-cycle-edge research-cycle-edge--two" aria-hidden="true"></span>
        <div class="research-cycle-node research-cycle-node--computation">
          <h3>Computation</h3>
          <p class="research-cycle-theme">Formal properties &middot; evaluation &middot; optimization</p>
          <p class="research-cycle-question">What can be derived, evaluated, and optimized once collaboration is represented, and at what computational cost?</p>
        </div>
      </div>
    </figure>
  </section>

  <section class="research-section research-lenses" aria-labelledby="lenses-heading">
    <h2 id="lenses-heading" class="screen-reader-text">Definition, representation, and computation</h2>

    <article class="research-lens">
      <header>
        <h3>Definition</h3>
        <p>Interdependence, collective capability, and collaborative primitives</p>
      </header>
      <p class="research-lens-question">What constitutes collaboration among intelligent entities, and which primitives distinguish it from mere group behavior?</p>
      <p>Definition begins with candidate primitives rather than a settled checklist. The <a href="https://arxiv.org/abs/2403.16809">LLM-based digital twin</a> placed heterogeneous human feedback into a shared reward objective. <a href="https://arxiv.org/abs/2502.05453">Decentralized generative agents</a> organized shared and local memory for planning under dependency constraints. <a href="https://openreview.net/forum?id=T7OoS6t11c">CUBE</a> made collective capability a property of the task: some goals are individually infeasible. <a href="https://arxiv.org/abs/2603.00349">COOP<sup>2</sup></a> then formalized collaborative tasks through verifiable cooperative requirements. The <a href="https://openreview.net/forum?id=LGsed0QQVq">Five Ws survey</a> situated these questions across communication structures in MARL, emergent language, and LLM-based multi-agent systems.</p>
      <p>Across these systems, interdependencies emerge as agents interact and share, while heterogeneous capabilities can yield collective capabilities for individually infeasible tasks or efficiency gains. These are candidate collaborative primitives, not a finished definition; which others matter remains open.</p>
    </article>

    <article class="research-lens">
      <header>
        <h3>Representation</h3>
        <p>Expressiveness, generalizability, and scalability</p>
      </header>
      <p class="research-lens-question">What representational structure can capture emergent collaboration across tasks, teams, and scales—and under what assumptions?</p>
      <p><a href="https://arxiv.org/abs/2603.00309">DIG</a> represents agent interaction as event passing between activations in a bipartite graph, with minimal assumptions about organization or execution. <a href="https://arxiv.org/abs/2603.00349">COOP<sup>2</sup></a> represents multi-agent interaction with the environment as an interplay between symbolic reasoning and grounded transitions. <a href="https://arxiv.org/abs/2511.04646">DR. WELL</a> makes a related symbolic-grounded structure explicit through roles, plans, and a shared world model that changes as agents act.</p>
      <p>At a more abstract level, <a href="https://arxiv.org/abs/2607.27429">iCORE</a> couples a graph of observed cooperation with a graph of evolving obligations and the evidence connecting them. Each step exposes a different tradeoff: <i>expressiveness</i> asks how much unconstrained, adaptive collaboration is captured; <i>generalizability</i>, what transfers versus must be redefined; and <i>scalability</i>, how complexity grows with system size. Their balance—and the assumptions each representation requires—remains open.</p>
    </article>

    <article class="research-lens">
      <header>
        <h3>Computation</h3>
        <p>Formal properties, evaluation, and optimization</p>
      </header>
      <p class="research-lens-question">What can be derived, evaluated, and optimized once collaboration is represented, and at what computational cost?</p>
      <p>A representation becomes useful when it supports questions that final task success cannot answer. <a href="https://arxiv.org/abs/2603.00309">DIG</a> makes reachability and progress failures visible in an event-activation graph, then supports online healing through information injection and rerouting. <a href="https://arxiv.org/abs/2603.00349">COOP<sup>2</sup></a> uses grounded task transitions to evaluate constraints; predicted violations open targeted communication channels for replanning. <a href="https://arxiv.org/abs/2607.27429">iCORE</a> formalizes work soundness and assignment stability in coupled cooperation-obligation graphs; their joint satisfaction quantifies state quality and yields a conditional performance bound.</p>
      <p>Together, these projects sharpen three roles for computation. <i>Formal properties</i> characterize feasibility, optimality, guarantees, and complexity. <i>Evaluation</i> quantifies collaborative states and links contributions to collective outcomes. <i>Optimization</i> improves outcomes at both agent and collective levels. The open question is which claims and interventions remain tractable as tasks, teams, and representations grow. Failures of evaluation or guarantees also expose what a representation is missing and feed back into the definition of collaboration.</p>
    </article>
  </section>

  <section class="research-section research-works" aria-labelledby="work-heading">
    <h2 id="work-heading" class="screen-reader-text">Research works</h2>

    <div class="research-work-list">
      <article id="work-icore" class="research-work research-work--icore">
        <div class="research-work-copy">
          <p class="research-work-meta">2026 &middot; Preprint, under review</p>
          <h3>Auditing Emergent LLM-Agent Collaboration through Cooperation-Obligation Coupling</h3>
          <p>Represents emergent collaboration through coupled cooperation-obligation graphs that formalize work soundness and assignment stability. Their joint satisfaction quantifies state quality and yields a conditional performance bound.</p>
          <p class="research-work-links"><a href="https://arxiv.org/abs/2607.27429">Paper</a></p>
        </div>
        <figure class="research-work-figure research-work-figure--icore" aria-labelledby="icore-figure-caption">
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
          <figcaption id="icore-figure-caption"><i>G</i> interaction &middot; <i>Q</i> obligation &middot; <i>&Pi;</i> evidence-backed coupling</figcaption>
        </figure>
      </article>

      <article id="work-coop2" class="research-work">
        <div class="research-work-copy">
          <p class="research-work-meta">2026 &middot; Preprint, under review</p>
          <h3>COOP<sup>2</sup>: Defining, Observing, and Repairing Cooperation in LLM Multi-Agent Systems</h3>
          <p>Defines collaborative tasks through verifiable requirements and connects symbolic agent communication to grounded environment transitions. Predicted constraint violations open targeted communication channels for replanning.</p>
          <p class="research-work-links"><a href="https://arxiv.org/abs/2603.00349">Paper</a><a href="/coop2/">Project page</a></p>
        </div>
        <figure class="research-work-figure">
          <img src="/coop2/figs/overview.png" alt="COOP squared connects symbolic agent activity with grounded environment execution." loading="lazy">
        </figure>
      </article>

      <article id="work-dig" class="research-work">
        <div class="research-work-copy">
          <p class="research-work-meta">2026 &middot; Preprint, under review</p>
          <h3>DIG to Heal: Scaling General-Purpose Agent Collaboration via Explainable Dynamic Decision Paths</h3>
          <p>Represents asynchronous multi-agent execution as a time-evolving graph of agent activations and events. The graph exposes reachability and progress failures and supports online healing through information injection and rerouting.</p>
          <p class="research-work-links"><a href="https://github.com/HappyEureka/dig">Repository</a><a href="https://arxiv.org/abs/2603.00309">Paper</a><a href="/dig/">Project page</a></p>
        </div>
        <figure class="research-work-figure">
          <img src="/dig/figs/fig2_new.png" alt="Dynamic Interaction Graph representation of agent activations and events." loading="lazy">
        </figure>
      </article>

      <article id="work-five-ws" class="research-work">
        <div class="research-work-copy">
          <p class="research-work-meta">2026 &middot; TMLR &middot; Survey Certification</p>
          <h3>The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why: A Survey from MARL to Emergent Language and LLMs</h3>
          <p>Surveys communication structures across MARL, emergent language, and LLM-based multi-agent systems through who talks to whom, when, what, and why. It reveals how organizational assumptions are often built into communication mechanisms rather than collaboration examined directly.</p>
          <p class="research-work-links"><a href="https://openreview.net/forum?id=LGsed0QQVq">Paper</a></p>
        </div>
        <figure class="research-work-figure research-work-figure--five-ws">
          <img src="/assets/images/research/five-ws-figure-11.png" alt="Figure 11 from the Five Ws survey: an overview of LLM-agent components, multi-agent communication designs, applications, and challenges." loading="lazy">
        </figure>
      </article>

      <article id="work-drwell" class="research-work">
        <div class="research-work-copy">
          <p class="research-work-meta">2025 &middot; NeurIPS LAW Workshop</p>
          <h3>DR. WELL: Dynamic Reasoning and Learning with Symbolic World Model for Embodied LLM-Based Multi-Agent Collaboration</h3>
          <p>Coordinates embodied agents through two phases: agents negotiate and commit to roles, then independently execute symbolic plans grounded in a shared world model. Working above raw trajectories makes collaboration more reusable and interpretable while allowing the world model to improve across episodes.</p>
          <p class="research-work-links"><a href="https://arxiv.org/abs/2511.04646">Paper</a><a href="https://narjesno.github.io/DR.WELL/">Project page</a></p>
        </div>
        <figure class="research-work-figure research-work-figure--drwell">
          <img src="/assets/images/research/drwell-overview.png" alt="DR. WELL overview: agents negotiate roles, execute symbolic plans, revise a shared world model, and validate plans in the environment." loading="lazy">
        </figure>
      </article>

      <article id="work-cube" class="research-work">
        <div class="research-work-copy">
          <p class="research-work-meta">2025 &middot; NeurIPS SEA Workshop</p>
          <h3>CUBE: Collaborative Multi-Agent Block-Pushing Environment for Collective Planning with LLM Agents</h3>
          <p>Designs weighted blocks, force, congestion, collisions, and timing so task-induced dependencies and collective capability become explicit. Some goals are individually infeasible, allowing collaboration to be studied as a property of the task rather than only of the policy.</p>
          <p class="research-work-links"><a href="https://openreview.net/forum?id=T7OoS6t11c">Paper</a><a href="/cube/">Project page</a></p>
        </div>
        <figure class="research-work-figure">
          <img src="/cube/static/images/embodied_constraints.png" alt="Physical constraints in the CUBE block-pushing environment." loading="lazy">
        </figure>
      </article>

      <article id="work-damcs" class="research-work">
        <div class="research-work-copy">
          <p class="research-work-meta">2025 &middot; AAAI MARW Workshop</p>
          <h3>LLM-Powered Decentralized Generative Agents with Adaptive Hierarchical Knowledge Graph for Cooperative Planning</h3>
          <p class="research-work-recognition"><a href="https://rdi.berkeley.edu/llm-agents-hackathon/">First Place (tie), Decentralized and Multi-Agents Track</a> &middot; Berkeley RDI LLM Agents MOOC Hackathon</p>
          <p>Introduces DAMCS, whose adaptive hierarchical knowledge graph organizes multimodal experience into shared and local memory. Decentralized agents can reason from past interactions while sharing relevant knowledge rather than entire histories during long-horizon planning under dependency constraints.</p>
          <p class="research-work-links"><a href="https://github.com/13RENDA/Mcrafter_LLM_Agent">Repository</a><a href="https://arxiv.org/abs/2502.05453">Paper</a><a href="/damcs/">Project page</a></p>
        </div>
        <figure class="research-work-figure">
          <img src="/damcs/static/images/abstract.png" alt="Agents in Multi-Agent Crafter cooperate through structured memory and communication." loading="lazy">
        </figure>
      </article>

      <article id="work-digital-twin" class="research-work">
        <div class="research-work-copy">
          <p class="research-work-meta">2024 &middot; IEEE International Workshop on Foundation Models (FMSys) &middot; Co-located with CPS-IoT Week</p>
          <h3>An LLM-Based Digital Twin for Optimizing Human-in-the-Loop Systems</h3>
          <p>Uses an LLM-based digital twin to simulate heterogeneous human feedback for adaptive HVAC control. Aggregated occupant preferences enter the reward objective, making collective preference part of what the controller learns to optimize.</p>
          <p class="research-work-links"><a href="https://github.com/HappyEureka/LLM_digital_twin">Repository</a><a href="https://arxiv.org/abs/2403.16809">Paper</a></p>
        </div>
        <figure class="research-work-figure research-work-figure--digital-twin">
          <img src="/assets/images/research/digital-twin-figure-1.png" alt="Figure 1 from the digital-twin paper: simulated population dynamics and aggregated thermal preferences train an agent-in-the-loop controller for comfort and energy savings." loading="lazy">
        </figure>
      </article>
    </div>
  </section>

  <section class="research-section research-healthcare" aria-labelledby="healthcare-heading">
    <header class="research-healthcare-intro">
      <h2 id="healthcare-heading">Earlier Work</h2>
      <p class="research-healthcare-subtitle">Machine Learning for Healthcare</p>
      <p>Before focusing on multi-agent systems, I worked closely with clinicians on decision support and scarce-resource allocation across international, national, and local datasets. These projects moved from validating risk scores, to aligning predictions with clinical decision horizons, to estimating treatment effects when a potentially beneficial intervention cannot be given to every eligible patient.</p>
    </header>

    <div class="research-work-list research-work-list--healthcare">
      <article class="research-work research-work--text">
        <div class="research-work-copy">
          <p class="research-work-meta">2023 &middot; Journal of the American Medical Informatics Association</p>
          <h3>Multi-Horizon Predictive Models for Guiding Extracorporeal Resource Allocation in Critically Ill COVID-19 Patients</h3>
          <p>Developed calibrated predictions at multiple time horizons for critically ill COVID-19 patients, aligning risk estimates with when scarce ECMO allocation decisions must be made.</p>
          <p class="research-work-links"><a href="https://doi.org/10.1093/jamia/ocac256">Paper</a></p>
        </div>
      </article>

      <article class="research-work research-work--text">
        <div class="research-work-copy">
          <p class="research-work-meta">2023 &middot; ACM SIGKDD</p>
          <h3>Assisting Clinical Decisions for Scarcely Available Treatment via Disentangled Latent Representation</h3>
          <p>Used disentangled latent representations to separate prognostic factors from heterogeneous treatment effects, supporting decisions when treatment capacity is limited.</p>
          <p class="research-work-links"><a href="https://doi.org/10.1145/3580305.3599774">Paper</a></p>
        </div>
      </article>

      <article class="research-work research-work--text">
        <div class="research-work-copy">
          <p class="research-work-meta">2023 &middot; Artificial Organs</p>
          <h3>Validation of ECMO Mortality Prediction and Severity-of-Illness Scores in an International COVID-19 Cohort</h3>
          <p>Evaluated mortality prediction and severity-of-illness scores in an international COVID-19 cohort, testing how established tools behave across a diverse clinical population.</p>
          <p class="research-work-links"><a href="https://doi.org/10.1111/aor.14542">Paper</a></p>
        </div>
      </article>
    </div>
  </section>

  <p class="research-complete-record">Complete publication record on <a href="https://scholar.google.com/citations?hl=en&amp;user=HnhN3tYAAAAJ">Google Scholar</a>.</p>
</div>

---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
excerpt: "Definition, representation, and computation of collaboration in multi-agent systems."
---

<div class="research-page">
  <section class="research-intro">
    <p class="research-summary">From defining collaboration, to representing emergent structure, to computing what becomes possible.</p>
    <p class="research-description">
      Rather than assuming a known organizational structure, I study how collaboration unfolds as agents interact, tasks are created and transformed, interdependencies emerge, and individual contributions become collectively consequential. My current work develops these ideas through LLM-based multi-agent systems.
    </p>
    <p class="research-links">
      <a href="/publications/">Publications</a>
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
          <p class="research-cycle-theme">Interdependence &middot; collective capability &middot; emergent dynamics</p>
          <p class="research-cycle-question">What defines collaboration among intelligent entities, and what dynamics distinguish it from mere group behavior?</p>
        </div>
        <span class="research-cycle-edge research-cycle-edge--one" aria-hidden="true"></span>
        <div class="research-cycle-node research-cycle-node--representation">
          <h3>Representation</h3>
          <p class="research-cycle-theme">Expressiveness &middot; adaptivity &middot; scalability</p>
          <p class="research-cycle-question">How can emergent collaboration be represented without prescribing organization or scale?</p>
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
        <p>Interdependence, collective capability, and emergent dynamics</p>
      </header>
      <p class="research-lens-question">What defines collaboration among intelligent entities, and what dynamics distinguish it from mere group behavior?</p>
      <p>Definition here does not mean fixing collaboration in advance. I ask which relational or structural objects make an interaction genuinely collaborative. Agents may not be the only—or even the most useful—objects: tasks, artifacts, obligations, evidence, and the relations among them may be equally fundamental. My earlier systems approached this question through the dependencies a task creates. The <a href="#work-digital-twin">LLM-based digital twin</a> brought heterogeneous human preferences into a shared control objective. <a href="#work-damcs">Decentralized generative agents</a> then made adaptive hierarchical knowledge-graph memory central: long-horizon cooperation depends on how each agent organizes multimodal experience and selectively shares relevant knowledge, not simply on retaining or transmitting more information. <a href="#work-cube">CUBE</a> made interdependence unavoidable in the environment itself.</p>
      <p>The <a href="#work-five-ws">Five Ws survey</a> clarified a limitation running through much of multi-agent research: communication is often designed around a predefined objective or organization and then used as a proxy for collaboration. This shifted the question from how agents should communicate to what relational or structural conditions make their behavior genuinely collaborative in the first place.</p>
    </article>

    <article class="research-lens">
      <header>
        <h3>Representation</h3>
        <p>Expressiveness, adaptivity, and scalability</p>
      </header>
      <p class="research-lens-question">How can emergent collaboration be represented without prescribing organization or scale?</p>
      <p><a href="#work-dig">DIG</a> began from the need to observe collaboration without fixing roles or workflows in advance. Its evolving event-activation graph preserves asynchronous decision paths and exposes structural failures, but a trace of what happened does not by itself say what work remains or who is responsible for it. <a href="#work-coop2">COOP<sup>2</sup></a> added grounding: it connects language-level plans and communication to task progress and explicit cooperative constraints.</p>
      <p><a href="#work-icore">iCORE</a> takes the next step by representing observable interaction, evolving work, assignment, and evidence together as <i>X = (G, Q, &Pi;)</i>. The progression is from recording interaction, to grounding it in the task, to treating collaboration as an auditable relational object that can change with the task and the team rather than inherit a fixed organization. These representational distinctions also feed back into Definition: the need to represent work, assignment, and evidence shows why interaction alone is not the right primitive.</p>
    </article>

    <article class="research-lens">
      <header>
        <h3>Computation</h3>
        <p>Formal properties, evaluation, and optimization</p>
      </header>
      <p class="research-lens-question">What can be derived, evaluated, and optimized once collaboration is represented, and at what computational cost?</p>
      <p>A representation becomes useful when it supports questions that final task success cannot answer. <a href="#work-dig">DIG</a> turns recurring structural patterns into diagnostics for lost, duplicated, stalled, or prematurely terminated work. <a href="#work-coop2">COOP<sup>2</sup></a> moves from diagnosis to intervention by testing cooperative constraints and opening targeted repair when a plan is likely to fail.</p>
      <p><a href="#work-icore">iCORE</a> moves further toward formal guarantees: it asks whether active work is soundly justified and whether assignments are stable, and connects local checks to global properties under stated conditions. Together these projects trace a progression from observing failure, to repairing it, to determining what can be certified or optimized—and when those computations remain tractable. Failed evaluations and guarantees feed back again, exposing what is missing from the representation and sharpening the definition of collaboration.</p>
    </article>
  </section>

  <section class="research-section research-works" aria-labelledby="work-heading">
    <h2 id="work-heading" class="screen-reader-text">Research works</h2>

    <div class="research-work-list">
      <article id="work-icore" class="research-work research-work--icore">
        <div class="research-work-copy">
          <p class="research-work-meta">2026 &middot; Preprint</p>
          <h3>Auditing Emergent LLM-Agent Collaboration through Cooperation-Obligation Coupling</h3>
          <p>Studies how observed interactions can be coupled with the work agents are responsible for and the evidence supporting each work-state transition. The resulting representation supports questions about soundness, responsibility, and assignment.</p>
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
          <p class="research-work-meta">2026 &middot; Preprint</p>
          <h3>COOP<sup>2</sup>: Defining, Observing, and Repairing Cooperation in LLM Multi-Agent Systems</h3>
          <p>Connects natural-language plans and communication to grounded task progress. Cooperative constraints make it possible to examine where a group fails to progress and whether targeted revision helps.</p>
          <p class="research-work-links"><a href="https://arxiv.org/abs/2603.00349">Paper</a><a href="/coop2/">Project page</a></p>
        </div>
        <figure class="research-work-figure">
          <img src="/coop2/figs/overview.png" alt="COOP squared connects symbolic agent activity with grounded environment execution." loading="lazy">
        </figure>
      </article>

      <article id="work-dig" class="research-work">
        <div class="research-work-copy">
          <p class="research-work-meta">2026 &middot; Preprint</p>
          <h3>DIG to Heal: Scaling General-purpose Agent Collaboration via Explainable Dynamic Decision Paths</h3>
          <p>Represents asynchronous multi-agent execution as a time-evolving graph of agent activations and events. The graph is used to locate structural patterns associated with lost, duplicated, stalled, or prematurely terminated work.</p>
          <p class="research-work-links"><a href="https://arxiv.org/abs/2603.00309">Paper</a><a href="/dig/">Project page</a></p>
        </div>
        <figure class="research-work-figure">
          <img src="/dig/figs/fig2_new.png" alt="Dynamic Interaction Graph representation of agent activations and events." loading="lazy">
        </figure>
      </article>

      <article id="work-five-ws" class="research-work research-work--text">
        <div class="research-work-copy">
          <p class="research-work-meta">2026 &middot; Transactions on Machine Learning Research</p>
          <h3>The Five Ws of Multi-Agent Communication: A Survey from MARL to Emergent Language and LLMs</h3>
          <p>Organizes multi-agent communication around who communicates with whom, when, what, and why. The survey shows how collaboration is often operationalized through developer-specified objectives or organization rather than treated as a first-class phenomenon.</p>
          <p class="research-work-links"><a href="https://openreview.net/forum?id=LGsed0QQVq">Paper</a></p>
        </div>
      </article>

      <article id="work-cube" class="research-work">
        <div class="research-work-copy">
          <p class="research-work-meta">2025 &middot; NeurIPS SEA Workshop</p>
          <h3>CUBE: Collaborative Multi-Agent Block-Pushing Environment</h3>
          <p>A lightweight environment in which weighted blocks, force, congestion, collisions, and timing create explicit dependencies among agents. It provides symbolic and primitive interfaces for studying collective planning.</p>
          <p class="research-work-links"><a href="https://openreview.net/forum?id=T7OoS6t11c">Paper</a><a href="/cube/">Project page</a></p>
        </div>
        <figure class="research-work-figure">
          <img src="/cube/static/images/embodied_constraints.png" alt="Physical constraints in the CUBE block-pushing environment." loading="lazy">
        </figure>
      </article>

      <article id="work-damcs" class="research-work">
        <div class="research-work-copy">
          <p class="research-work-meta">2025 &middot; AAAI MARW Workshop</p>
          <h3>Decentralized Generative Agents for Cooperative Planning</h3>
          <p>Introduces DAMCS, with adaptive hierarchical knowledge-graph memory as its central mechanism. The memory organizes multimodal experience across levels so decentralized agents can reason from past interactions, while structured communication lets them share relevant knowledge rather than entire histories during long-horizon planning.</p>
          <p class="research-work-links"><a href="https://arxiv.org/abs/2502.05453">Paper</a><a href="/damcs/">Project page</a></p>
        </div>
        <figure class="research-work-figure">
          <img src="/damcs/static/images/abstract.png" alt="Agents in Multi-Agent Crafter cooperate through structured memory and communication." loading="lazy">
        </figure>
      </article>

      <article id="work-digital-twin" class="research-work research-work--text">
        <div class="research-work-copy">
          <p class="research-work-meta">2024 &middot; IEEE FMSys</p>
          <h3>An LLM-Based Digital Twin for Optimizing Human-in-the-Loop Systems</h3>
          <p>Uses an LLM-based digital twin to simulate heterogeneous human feedback for adaptive HVAC control, with collective occupant preferences encoded in the learning objective.</p>
          <p class="research-work-links"><a href="https://arxiv.org/abs/2403.16809">Paper</a></p>
        </div>
      </article>
    </div>
  </section>

  <p class="research-complete-record">The <a href="/publications/">publications page</a> includes the complete record.</p>
</div>

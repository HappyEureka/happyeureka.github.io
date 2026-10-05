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
    <p class="research-summary">From what constitutes collaboration, to how to represent it structurally, whether predefined or emergent, to what that structure makes computationally possible, and at what cost. Collaboration is itself agnostic to team members and team size; my current work focuses on its realization among LLM agents.</p>
  </section>

  {% include research-fun.html %}

  <section class="research-section research-directions" aria-labelledby="directions-heading">
    <h2 id="directions-heading" class="research-divider">Research agenda</h2>

    <figure class="research-cycle" aria-label="Definition, representation, and computation form a triangle of two-way relations.">
      <div class="research-cycle-diagram">
        <div class="research-cycle-node research-cycle-node--definition">
          <h3>Definition</h3>
          <p class="research-cycle-theme">Interdependence &middot; collective capability &middot; collaborative primitives</p>
        </div>
        <div class="research-cycle-sides" aria-hidden="true">
          <span class="research-cycle-edge research-cycle-edge--left"></span>
          <span class="research-cycle-edge research-cycle-edge--right"></span>
        </div>
        <div class="research-cycle-node research-cycle-node--representation">
          <h3>Representation</h3>
          <p class="research-cycle-theme">Expressiveness &middot; generalizability &middot; scalability</p>
        </div>
        <span class="research-cycle-edge research-cycle-edge--base" aria-hidden="true"></span>
        <div class="research-cycle-node research-cycle-node--computation">
          <h3>Computation</h3>
          <p class="research-cycle-theme">Formal properties &middot; evaluation &middot; optimization</p>
        </div>
      </div>
    </figure>
  </section>

  <section class="research-section research-lenses" aria-labelledby="lenses-heading">
    <h2 id="lenses-heading" class="screen-reader-text">Definition, representation, and computation</h2>

    <article class="research-lens">
      <p class="research-lens-lead"><strong class="research-lens-name">Definition.</strong> <em class="research-lens-question">What constitutes collaboration among intelligent entities, and which primitives distinguish it from mere group behavior?</em></p>
      <p>Collaboration can be a property of the task itself: in <a href="https://openreview.net/forum?id=T7OoS6t11c">CUBE</a>, some goals are individually infeasible. <a href="https://arxiv.org/abs/2603.00349">COOP<sup>2</sup></a> turns that into a formal requirement, with four categories of constraints that guard cooperative progress. <a href="/tea/">TEA</a> defines the collaboration policy, separating the behavior it prescribes from the behavior that emerges. Earlier steps came from the <a href="https://arxiv.org/abs/2403.16809">LLM-based digital twin</a>, <a href="https://arxiv.org/abs/2502.05453">decentralized generative agents</a>, and the <a href="https://openreview.net/forum?id=LGsed0QQVq">Five Ws survey</a>.</p>
      <p>Interdependence and collective capability are candidate primitives; which others matter remains open.</p>
    </article>

    <article class="research-lens">
      <p class="research-lens-lead"><strong class="research-lens-name">Representation.</strong> <em class="research-lens-question">What representational structure can capture collaboration, whether predefined or emergent, across tasks, teams, and scales—and under what assumptions?</em></p>
      <p>Collaboration can be recorded without assuming how agents organize. <a href="https://arxiv.org/abs/2603.00309">DIG</a> captures it as event passing between activations, and <a href="/tea/">TEA</a> adds the tasks agents create and revise and the shared environment they act in. <a href="https://arxiv.org/abs/2603.00349">COOP<sup>2</sup></a> and <a href="https://arxiv.org/abs/2511.04646">DR. WELL</a> instead couple symbolic reasoning with grounded transitions through roles, plans, and a shared world model, and <a href="https://arxiv.org/abs/2607.27429">iCORE</a> links observed cooperation to evolving obligations and the evidence connecting them.</p>
      <p>Each exposes a tradeoff among <i>expressiveness</i>, <i>generalizability</i>, and <i>scalability</i>; their balance remains open.</p>
    </article>

    <article class="research-lens">
      <p class="research-lens-lead"><strong class="research-lens-name">Computation.</strong> <em class="research-lens-question">What can be derived, evaluated, and optimized once collaboration is represented, and at what computational cost?</em></p>
      <p>A representation makes visible and repairable the failures that final task success hides. <a href="https://arxiv.org/abs/2603.00309">DIG</a> exposes reachability and progress failures and heals them online through information injection and rerouting, and <a href="https://arxiv.org/abs/2603.00349">COOP<sup>2</sup></a> uses predicted constraint deficits to open targeted communication. Representation also supports guarantees and improvement: <a href="https://arxiv.org/abs/2607.27429">iCORE</a> formalizes work soundness and assignment stability, yielding a conditional performance bound, and <a href="/tea/">TEA</a> recovers the realized topology and candidate rules from the record, so Infuse can decide what to keep, add, revise, or leave open and propose an updated policy.</p>
      <p>The open question is which claims and interventions stay tractable as tasks, teams, and representations grow. Where they fail, they expose what a representation is missing and feed back into the definition.</p>
    </article>
  </section>

</div>

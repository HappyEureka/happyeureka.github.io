---
layout: archive
title: "Open Source"
permalink: /open-source/
author_profile: true
hide_archive_title: true
excerpt: "Tools and environments from my research, released for others to inspect, use, and extend."
---

<div class="open-source-page">
  <header class="open-source-intro">
    <h1>Open Source</h1>
    <p class="open-source-description">I am constantly inspired by open-source projects and grateful for the openness behind them. Many of my projects began with ideas and tools shared by others. Hope something here can also help!</p>
  </header>

  <section class="open-source-coming" aria-label="Future open-source releases">
    <p>More is coming.</p>
  </section>

  <main>
    <div class="open-source-releases">
      <article class="open-source-release" aria-labelledby="coop2-release-title">
        <div class="open-source-release-copy">
          <p class="open-source-release-meta">Python &middot; MIT License</p>
          <h2 id="coop2-release-title">COOP<sup>2</sup> <span>Observable cooperation in LLM multi-agent systems</span></h2>
          <p>Code for connecting the cognitive activity of LLM agents to grounded environment actions and cooperative task progress.</p>

          <dl class="open-source-capabilities">
            <div>
              <dt>Define</dt>
              <dd>Model agent dynamics across cognitive and primitive layers alongside the task requirements that guard progress.</dd>
            </div>
            <div>
              <dt>Observe</dt>
              <dd>Measure task progress, coordination cost, and constraint deficits as cooperation unfolds.</dd>
            </div>
            <div>
              <dt>Explore</dt>
              <dd>Run CUBE and MA-Crafter experiments, including the paper's COOP<sup>2</sup>-Repair case study.</dd>
            </div>
          </dl>

          <p class="open-source-links"><a href="https://github.com/HappyEureka/coop2-llm-mas">Repository</a><a href="https://arxiv.org/abs/2603.00349">Paper</a><a href="/coop2/">Project page</a></p>
        </div>

        <figure class="open-source-release-figure">
          <img src="/coop2/figs/overview.png" alt="COOP squared connects cognitive agent activity, grounded environment actions, and cooperative task requirements." loading="lazy">
          <figcaption>Agent dynamics and task requirements make the cooperation process observable.</figcaption>
        </figure>
      </article>

      <article class="open-source-release" aria-labelledby="dig-release-title">
        <div class="open-source-release-copy">
          <p class="open-source-release-meta">Python &middot; MIT License</p>
          <h2 id="dig-release-title">DIG <span>Dynamic Interaction Graph</span></h2>
          <p>DIG records emergent multi-agent execution as a time-evolving graph of agent activations and events. It is agnostic to the language model, environment, and number of agents.</p>

          <dl class="open-source-capabilities">
            <div>
              <dt>Observe</dt>
              <dd>Wrap agents from an existing framework, or let DIG deliver events itself.</dd>
            </div>
            <div>
              <dt>Inspect</dt>
              <dd>Trace events, activations, reactions, routing, and lineage as a run unfolds.</dd>
            </div>
            <div>
              <dt>Heal</dt>
              <dd>Detect structural failures and record information injection or rerouting interventions.</dd>
            </div>
          </dl>

          <p class="open-source-links"><a href="https://github.com/HappyEureka/dig">Repository</a><a href="https://arxiv.org/abs/2603.00309">Paper</a><a href="/dig/">Project page</a></p>
        </div>

        <figure class="open-source-release-figure">
          <img src="/dig/figs/fig2_new.png" alt="DIG represents multi-agent execution using agent activations and the events that flow between them." loading="lazy">
          <figcaption>Agent activations and events form a dynamic, inspectable record of collaboration.</figcaption>
        </figure>
      </article>

      <article class="open-source-release" aria-labelledby="mcrafter-release-title">
        <div class="open-source-release-copy">
          <p class="open-source-release-meta">Python &middot; Multi-agent simulation</p>
          <h2 id="mcrafter-release-title">Multi-Agent Crafter <span>Decentralized generative agents</span></h2>
          <p>A Minecraft-inspired environment for studying LLM agents that plan, remember, share resources, and work toward a collective objective.</p>

          <dl class="open-source-capabilities">
            <div>
              <dt>Simulate</dt>
              <dd>Run configurable teams in a resource-gathering and crafting environment.</dd>
            </div>
            <div>
              <dt>Remember</dt>
              <dd>Use persistent memory and knowledge graphs for long-horizon planning.</dd>
            </div>
            <div>
              <dt>Observe</dt>
              <dd>Follow individual agents or the full team through a multi-view interface.</dd>
            </div>
          </dl>

          <p class="open-source-links"><a href="https://github.com/13RENDA/Mcrafter_LLM_Agent">Repository</a><a href="https://arxiv.org/abs/2502.05453">Paper</a><a href="/damcs/">Project page</a></p>
        </div>

        <figure class="open-source-release-figure">
          <img src="/damcs/static/images/abstract.png" alt="Multiple LLM agents collaborate in the Multi-Agent Crafter environment." loading="lazy">
          <figcaption>Agents coordinate resource gathering and crafting through shared and local memory.</figcaption>
        </figure>
      </article>

      <article class="open-source-release" aria-labelledby="digital-twin-release-title">
        <div class="open-source-release-copy">
          <p class="open-source-release-meta">Python &middot; Jupyter notebooks</p>
          <h2 id="digital-twin-release-title">LLM-Based Digital Twin <span>Human-in-the-loop control</span></h2>
          <p>Code for simulating heterogeneous human feedback and training HVAC controllers around collective comfort and energy use.</p>

          <dl class="open-source-capabilities">
            <div>
              <dt>Simulate</dt>
              <dd>Model a population with heterogeneous thermal preferences.</dd>
            </div>
            <div>
              <dt>Control</dt>
              <dd>Run centralized and decentralized controller experiments.</dd>
            </div>
            <div>
              <dt>Evaluate</dt>
              <dd>Reproduce analysis, visualization, and confidence-interval workflows.</dd>
            </div>
          </dl>

          <p class="open-source-links"><a href="https://github.com/HappyEureka/LLM_digital_twin">Repository</a><a href="https://arxiv.org/abs/2403.16809">Paper</a></p>
        </div>

        <figure class="open-source-release-figure">
          <img src="/assets/images/research/digital-twin-figure-1.png" alt="An LLM-based digital twin simulates population feedback used to train an HVAC controller." loading="lazy">
          <figcaption>Simulated population dynamics connect human feedback to controller training.</figcaption>
        </figure>
      </article>
    </div>

  </main>
</div>

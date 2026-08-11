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
    <p class="open-source-summary">Talk is cheap...</p>
    <p class="open-source-description">I am constantly inspired by open-source projects and grateful for the openness behind them. Many of my projects began with ideas and tools shared by others. I hope something here can become a starting point for someone else.</p>
  </header>

  <main>
    <article class="open-source-release" aria-labelledby="dig-release-title">
      <div class="open-source-release-copy">
        <p class="open-source-release-meta">Available now &middot; Python &middot; MIT License</p>
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
  </main>
</div>

/* KIS academic interactions: generic, scenario-data driven. No Modbus-specific topology is hard-coded here. */
(function () {
  "use strict";
  const source = document.getElementById("kisScenarioData");
  if (!source) return;
  let scenes = [];
  try { scenes = JSON.parse(source.textContent).scenarios || []; }
  catch (error) { console.error("Invalid course scenarios", error); return; }
  const byId = new Map(scenes.map(scene => [scene.id, scene]));
  const SVG = "http://www.w3.org/2000/svg";
  function element(tag, attrs, parent, content) {
    const node = document.createElementNS(SVG, tag);
    Object.entries(attrs || {}).forEach(function (pair) { node.setAttribute(pair[0], String(pair[1])); });
    if (content !== undefined) node.textContent = content;
    if (parent) parent.appendChild(node);
    return node;
  }
  function drawScenario(id, stageId) {
    const scene = byId.get(id);
    if (!scene) return;
    const stage = scene.stages.find(s => s.id === stageId) || scene.stages[0];
    const display = document.querySelector('[data-scenario-display="' + id + '"]');
    const note = document.querySelector('[data-scenario-note="' + id + '"]');
    if (!display || !note) return;
    display.replaceChildren();
    const svg = element("svg", {viewBox:"0 0 900 235", role:"img", "aria-label":scene.title + ": " + stage.label}, display);
    const map = new Map(stage.nodes.map(n => [n.id, n]));
    stage.links.forEach(function(link) {
      const from = map.get(link.from), to = map.get(link.to);
      if (!from || !to) return;
      const x1 = from.x + 76, x2 = to.x - 76, y1 = from.y, y2 = to.y;
      const mid = (x1 + x2) / 2;
      element("path", {d:"M " + x1 + " " + y1 + " C " + mid + " " + y1 + ", " + mid + " " + y2 + ", " + x2 + " " + y2, class:"scenario-link"}, svg);
      element("text", {x:mid, y:((y1+y2)/2)-16, class:"scenario-linklabel", "text-anchor":"middle"}, svg, link.label || "");
    });
    stage.nodes.forEach(function(n) {
      const cls = n.type === "bad" ? "scenario-device bad" : n.type === "gateway" ? "scenario-device gateway" : n.type === "client" ? "scenario-device client" : "scenario-device sensor";
      element("rect", {x:n.x-76,y:n.y-27,width:152,height:54,rx:9,class:cls}, svg);
      element("text", {x:n.x,y:n.y+4,class:"scenario-device-label","text-anchor":"middle"}, svg, n.label);
    });
    note.textContent = (stage.measurement ? stage.measurement + " · " : "") + stage.summary;
  }
  document.querySelectorAll("[data-scenario]").forEach(function(widget) {
    const id = widget.getAttribute("data-scenario"), scene = byId.get(id);
    const select = widget.querySelector("select[data-scenario-select]");
    if (!scene || !select || !Array.isArray(scene.stages) || !scene.stages.length) return;
    select.replaceChildren();
    scene.stages.forEach(function(stage) {
      const opt = document.createElement("option");
      opt.value = stage.id;
      opt.textContent = stage.label;
      select.appendChild(opt);
    });
    select.value = scene.default_stage || scene.stages[0].id;
    select.addEventListener("change", function() { drawScenario(id, select.value); });
    drawScenario(id, select.value);
  });
  const regInput = document.getElementById("regDisplay");
  if (regInput) {
    const output = document.getElementById("regOffset"), message = document.getElementById("regResult");
    const update = function() {
      const raw = regInput.value.trim(), value = Number(raw);
      if (!raw || !Number.isInteger(value) || value < 40001 || value > 49999) {
        output.textContent = "—";
        message.textContent = "Enter a whole-number holding-register label from 40001 to 49999.";
        return;
      }
      const offset = value - 40001;
      output.textContent = String(offset);
      message.textContent = value + " → offset " + offset + " using the conventional 4xxxx label convention.";
    };
    regInput.addEventListener("input", update);
    update();
  }
  document.querySelectorAll("[data-open-calc]").forEach(function(button) {
    button.addEventListener("click", function() {
      const target = button.getAttribute("data-open-calc");
      const link = document.querySelector('[data-calc="' + target + '"]');
      if (link) link.click();
    });
  });
})();

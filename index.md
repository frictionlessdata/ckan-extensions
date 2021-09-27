# CKAN Extensions

## Introduction

**CKAN** is an open-source DMS (data management system) for powering data hubs and data portals. CKAN makes it easy to publish, share and use data. It powers catalog.data.gov, open.canada.ca/data, data.humdata.org among many other sites. We have [collected](data.html) and sorted by the stars count all the CKAN extensions available as repositories on Github and having at lease 1 star. Read more about [CKAN](https://ckan.org/). If you are interested in contributing to this livemark please follow this [guide](contrib.html).

## Extensions

```html markup
{% for row in frictionless.extract('data/extensions.csv') %}
<div class="item">
  <div class="item-content">
    <h3>{{ row.title or row.code }}</h3>
    <p>{{ row.description or 'Description is not provided'}}</p>
    <p>
      <a class="item-content-link" href="https://github.com/{{ row.user}}/{{row.repo }}" target="_blank">
        Github <span class="fa fa-external-link-alt"></span>
      </a>
    </p>
  </div>
  <div class="item-stars">
    <span class="fa-stack fa-2x">
      <i class="fas fa-stack-2x fa-star fa-inverse item-stars-icon"></i>
      <i class="fas fa-stack-1x item-stars-count">{{ row.stars }}</i>
    </span>
  </div>
</div>
{% endfor %}
```

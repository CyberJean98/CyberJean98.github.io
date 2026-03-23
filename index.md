---
layout: home
---

Welcome to my portfolio! Documenting my transition from **Lead Line Cook** at Via Italian Table to **Cybersecurity Professional**.

### Latest Posts
{% for post in site.posts %}
* [{{ post.title }}]({{ post.url }}) - {{ post.date | date_to_string }}
{% endfor %}

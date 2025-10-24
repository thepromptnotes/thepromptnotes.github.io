---
layout: default
title: Archive
permalink: /archive/
---

# Archive

All posts, organized by year.

{% assign postsByYear = site.posts | group_by_exp:"post", "post.date | date: '%Y'" %}
{% for year in postsByYear %}
<div class="year-group">
    <h2>{{ year.name }}</h2>
    <ul class="archive-list">
        {% for post in year.items %}
        <li>
            <span class="archive-date">{{ post.date | date: "%b %d" }}</span>
            <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        </li>
        {% endfor %}
    </ul>
</div>
{% endfor %}

<style>
    .year-group {
        margin: 2em 0;
    }
    
    .year-group h2 {
        font-size: 1.5em;
        color: #555;
        margin-bottom: 1em;
    }
    
    .archive-list {
        list-style: none;
        padding: 0;
    }
    
    .archive-list li {
        margin: 0.8em 0;
        display: flex;
        align-items: baseline;
    }
    
    .archive-date {
        color: #999;
        font-size: 0.9em;
        min-width: 60px;
        margin-right: 1em;
    }
    
    .archive-list a {
        flex: 1;
    }
</style>

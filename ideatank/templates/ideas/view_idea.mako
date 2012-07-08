<%inherit file="../base/master.mako" />

<h2>${idea.title}</h2>

<h3>Details</h3>
<p>
    ${idea.description}
</p>

<div class="idea-meta">
    <p><span>Submitted by: </span>${idea.author} <span>on</span> ${idea.created_at}</p>
    <p><span>Category: </span>${idea.category.cat_name.capitalize()}</p>
</div>
<hr />
<a href="${request.route_url('ideas')}" class="btn"><i class="icon-arrow-left"></i> Back to all ideas</a>
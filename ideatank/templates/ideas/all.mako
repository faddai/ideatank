<%inherit file="../base/master.mako" />

<h2>All ideas</h2>
<ul>
% for idea in ideas:
    <li><a href="${request.application_url}/ideas/${idea.id}">${idea.title}</a> posted in
    <a href="${request.application_url}/ideas/category/${idea.category.cat_id}">${idea.category.cat_name.capitalize()}</a>    
    </li>
% endfor
</ul>


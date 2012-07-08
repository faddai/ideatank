<%inherit file="../base/master.mako"/>

<h2>Categories</h2>
<ul>
    % for cat in categories:
        <li><a href="${request.application_url}/ideas/category/${cat.cat_id}">${cat.cat_name}</a></li>
    % endfor
</ul>
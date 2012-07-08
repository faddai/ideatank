<%def name="get_categories(categories)">
    % for cat in categories:
        <li><a href="${request.application_url}/ideas/category/${cat.cat_id}">${cat.cat_name}</a></li>
    % endfor
</%def>
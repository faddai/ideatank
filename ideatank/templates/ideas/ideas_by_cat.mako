<%inherit file='../base/master.mako' />

<h2>Ideas posted in ${ideas}</h2>
<ul>
    % for idea in ideas:
        <li><a href="${request.application_url}/ideas/${idea.id}">${idea.title}</a></li>
    % endfor
</ul>
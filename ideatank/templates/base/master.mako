<%def name="get_categories()">
    % for cat in categories:
        <li><a href="${request.application_url}/ideas/category/${cat.cat_id}">${cat.cat_name}</a></li>
    % endfor
</%def>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>Ideas Tank</title>
        <link href="${request.static_url('ideatank:static/css/bootstrap.min.css')}" rel="stylesheet" />
        <link href="${request.static_url('ideatank:static/css/style.css')}" rel="stylesheet" />
    </head>
<body>
    
    <div class="container">
        <div class="hero-unit">
            <h1>ideaTank</h1>
            <p>A land of awesomeness, put on your creative cap and start cooking up great ideas. Submit your awesome ideas and get feedback from other users.</p>
            <p>
                <a href="${request.route_url('new_idea')}" class="btn btn-primary btn-large">Add an idea</a>
                <a href="${request.route_url('ideas')}" class="btn btn-large">View all ideas</a>
            </p>

        </div>
        <div class="content">
            <div class="span7">
                ${next.body()}
            </div>
            
            <div class="span4 well">
                <h2>Users</h2>
                <li><a href="${request.route_url('new_user')}">Register</a></li>
                <li><a href="${request.route_url('login_user')}">Login</a></li>
                
                <h2>Categories</h2>
                
                
            </div>
        </div>
    </div>
    
<script src="${request.static_url('ideatank:static/js/jquery.js')}"></script>
<script src="${request.static_url('ideatank:static/js/bootstrap.min.js')}"></script>
<script src="${request.static_url('ideatank:static/js/app.js')}"></script>
</body>
</html>

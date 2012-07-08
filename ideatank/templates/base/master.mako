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
        <div class="content">
            ${next.body()}
        </div>
    </div>
    
<script src="${request.static_url('ideatank:static/js/jquery.js')}"></script>
<script src="${request.static_url('ideatank:static/js/bootstrap.min.js')}"></script>
<script src="${request.static_url('ideatank:static/js/app.js')}"></script>
</body>
</html>

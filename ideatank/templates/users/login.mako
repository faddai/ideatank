<%inherit file="../base/master.mako" />
<h2>Login</h2>

<form action="${login_url}" method="POST">
    <label for="username">Username</label>
    <input type="text" name="username" id="username" required />

    <label for="password">Password</label>
    <input type="password" name="password" id="password" required />

    <p><input type="submit" name="form.submitted" value="Login" class="btn btn-primary btn-large" /></p>
</form>

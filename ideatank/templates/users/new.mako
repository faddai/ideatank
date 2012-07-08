<%inherit file="../base/master.mako" />

<h2>Register</h2>
<form action="${save_url}" method="POST">
    <label for="fname">First name</label>
    <input type="text" name="fname" id="fname" />

    <label for="lname">Last name</label>
    <input type="text" name="lname" id="lname" />

    <label for="email">Email Address</label>
    <input type="email" name="email" id="email" />

    <label for="username">Username</label>
    <input type="text" name="username" id="username" />

    <label for="password">Password</label>
    <input type="password" name="password" id="password" />
    <input type="password" name="passwordcfm" placeholder="Confirm Password" />
    
    <p><input type="submit" name="form.submitted" class="btn btn-primary btn-large" value="Register and start adding Awesome ideas" /></p>

</form>

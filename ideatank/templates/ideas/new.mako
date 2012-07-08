<%inherit file="../base/master.mako" />

<h2>Add new idea</h2>
<form action="${save_url}" method="POST">
    <label for="title">Title</label>
    <input type="text" name="title" id="title" />

    <label for="category">Category</label>
    <select name="category" id="category">
        <option value="">Choose category</option>
        <option value="1">Technology</option>
        <option value="2">Industrial</option>
        <option value="1">Technology</option>
        <option value="1">Technology</option>
        <option value="1">Technology</option>
    </select>

    <label for="description">Description</label>
    <textarea name="description" id="description"></textarea>

    <input type="submit" name="form.submitted" value="Add idea" />

</form>

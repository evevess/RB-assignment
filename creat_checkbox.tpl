//<p>Check all the languages you have proficiency in.</p>
//<form action="/new" method="POST">
//<input type="checkbox" id="name(alphabically)" value="name(alphabically)"><label for="name(alphabically)"> name(alphabically)</label><br>
//<input type="checkbox" id="age(ascending)" value="age(ascending)"><label for="age(ascending)"> age(ascending)</label><br>
//<input type="checkbox" id="age(descending)" value="age(descending)"><label for="age(descending)"> age(descending)</label><br>
//<input type="checkbox" id="salary(ascending)" value="salary(ascending)"><label for="salary(ascending)"> salary(ascending)</label><br>
//<input type="checkbox" id="salary(descending)" value="salary(descending)"><label for="salary(descending)"> salary(descending)</label><br>
//</form>


<p>Add a new case to the list:</p>
<form action="/new" method="GET">
    protocol: <input type="text" size="50" maxlength="50" name="protocol"><br>
    service: <input type="text" size="50" maxlength="50" name="service"><br>
    plugin: <input type="text" size="50" maxlength="100" name="plugin"><br>
    value: <input type="text" size="50" maxlength="100" name="value"><br>
    <input type="submit" name="add" value="Add to the list">
</form>

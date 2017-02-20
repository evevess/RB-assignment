%# disp_table.tpl
<p>The items are as follows:</p>
<table border="1">
%for r in rows:
  <tr>
  %for c in r:
    <td>{{c}}</td>
  %end
  </tr>
%end
</table>

<p>Please choose your sorting method.</p>
<form action="/new" method="POST">
<input type="checkbox" id="name(alphabically)" value=1><label for="name(alphabically)"> name(alphabically)</label><br>
<input type="checkbox" id="age(ascending)" value=2><label for="age(ascending)"> age(ascending)</label><br>
<input type="checkbox" id="age(descending)" value=3><label for="age(descending)"> age(descending)</label><br>
<input type="checkbox" id="salary(ascending)" value=4><label for="salary(ascending)"> salary(ascending)</label><br>
<input type="checkbox" id="salary(descending)" value=5><label for="salary(descending)"> salary(descending)</label><br>
<input type="submit" name="OK" value="OK">
</form>

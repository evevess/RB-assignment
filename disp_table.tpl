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
<form action='/origin', method='POST'>
<input type="checkbox" name="method1" value=1> name(alphabically)<br>
<input type="checkbox" name="method2" value=2> age(ascending)<br>
<input type="checkbox" name="method3" value=3> age(descending)<br>
<input type="checkbox" name="method4" value=4> salary(ascending)<br>
<input type="checkbox" name="method5" value=5> salary(descending)<br>
<input type="submit" name="submit" value="submit">
</form>


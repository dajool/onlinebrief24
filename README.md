# Installation

```pip install onlinebrief24``` (!!! Sorry, not yet !!!)

# Beispiele

```python
import onlinebrief24

c = onlinebrief24.Client('email@example.com', 'secret_password')
c.login()
c.upload('/tmp/filename1.pdf', duplex=False, color=False)
c.upload('/tmp/filename2.pdf', registered='insertion', envelope='c4')
c.disconnect()
```

## with-statement
```python
with onlinebrief24.Client('email@example.com', 'secret_password') as c:
    c.upload('/tmp/filename1.pdf', duplex=False, color=False)
    c.upload('/tmp/filename2.pdf', registered='insertion', envelope='c4')
```


## Optionen für Brief

<table width="100%">
  <tr>
    <th>Option</th>
    <th>Werte</th>
    <th>Vorbelegung</th>
    <th>Beschreibung</th>
  </tr>
  <tr>
    <td>
      <strong>color</strong>
    </td>
    <td>
      <ul>
        <li>True</li>
        <li>False</li>
      </ul>
    </td>
    <td>
      True
    </td>
    <td>
      Farbdruck ja/nein
    </td>
  </tr>
    
  <tr>
    <td>
      <strong>duplex</strong>
    </td>
    <td>
      <ul>
        <li>True</li>
        <li>False</li>
      </ul>
    </td>
    <td>
      True
    </td>
    <td>
      Duplexdruck ja/nein
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>envelope</strong>
    </td>
    <td>
      <ul>
        <li>din_lang</li>
        <li>c4</li>
      </ul>
    </td>
    <td>
      din_lang
    </td>
    <td>
      Umschlagformat. DIN lang oder C4.
    </td>
  </tr>

  <tr>
    <td>
      <strong>distribution</strong>
    </td>
    <td>
      <ul>
        <li>auto</li>
        <li>national</li>
        <li>international</li>
      </ul>
    </td>
    <td>
      auto
    </td>
    <td>
      Versandzone. Automatisch, National, International
    </td>
  </tr>

  <tr>
    <td>
      <strong>registered</strong>
    </td>
    <td>
      <ul>
        <li>None</li>
        <li>insertion</li>
        <li>standard</li>
        <li>personal</li>
      </ul>
    </td>
    <td>
      None
    </td>
    <td>
      Einschreiben: Nein, Einwurf-Einschreiben, Standard-Einschreiben, Einschreiben eigenhändig
    </td>
  </tr>

  <tr>
    <td>
      <strong>payment_slip</strong>
    </td>
    <td>
      <ul>
        <li>None</li>
        <li>national</li>
        <li>sepa</li>
      </ul>
    </td>
    <td>
      None
    </td>
    <td>
      Zahlschein: Kein Zahlschein, Inlands-Zahlschein, SEPA-Zahlschein
    </td>
  </tr>
  

</table>

## Copyright

All rights reserved.

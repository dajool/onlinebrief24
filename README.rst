Installation
============

``pip install onlinebrief24``

Beispiele
=========

.. code:: python

    import onlinebrief24

    c = onlinebrief24.Client('email@example.com', 'secret_password')
    c.login()
    c.upload('/tmp/filename1.pdf', duplex=False, color=False)
    c.upload('/tmp/filename2.pdf', registered='insertion', envelope='c4')
    c.disconnect()

with-statement
--------------

.. code:: python

    with onlinebrief24.Client('email@example.com', 'secret_password') as c:
        c.upload('/tmp/filename1.pdf', duplex=False, color=False)
        c.upload('/tmp/filename2.pdf', registered='insertion', envelope='c4')

Optionen für Brief
------------------

.. raw:: html

   <table width="100%">
     <tr>
       <th>

Option

.. raw:: html

   </th>
       <th>

Werte

.. raw:: html

   </th>
       <th>

Vorbelegung

.. raw:: html

   </th>
       <th>

Beschreibung

.. raw:: html

   </th>
     </tr>
     <tr>
       <td>
         

color

.. raw:: html

   </td>
       <td>
         <ul>
           <li>

True

.. raw:: html

   </li>
           <li>

False

.. raw:: html

   </li>
         </ul>
       </td>
       <td>
         

True

.. raw:: html

   </td>
       <td>
         

Farbdruck ja/nein

.. raw:: html

   </td>
     </tr>
       

.. raw:: html

   <tr>
       <td>
         

duplex

.. raw:: html

   </td>
       <td>
         <ul>
           <li>

True

.. raw:: html

   </li>
           <li>

False

.. raw:: html

   </li>
         </ul>
       </td>
       <td>
         

True

.. raw:: html

   </td>
       <td>
         

Duplexdruck ja/nein

.. raw:: html

   </td>
     </tr>
     

.. raw:: html

   <tr>
       <td>
         

envelope

.. raw:: html

   </td>
       <td>
         <ul>
           <li>

din\_lang

.. raw:: html

   </li>
           <li>

c4

.. raw:: html

   </li>
         </ul>
       </td>
       <td>
         

din\_lang

.. raw:: html

   </td>
       <td>
         

Umschlagformat. DIN lang oder C4.

.. raw:: html

   </td>
     </tr>

.. raw:: html

   <tr>
       <td>
         

distribution

.. raw:: html

   </td>
       <td>
         <ul>
           <li>

auto

.. raw:: html

   </li>
           <li>

national

.. raw:: html

   </li>
           <li>

international

.. raw:: html

   </li>
         </ul>
       </td>
       <td>
         

auto

.. raw:: html

   </td>
       <td>
         

Versandzone. Automatisch, National, International

.. raw:: html

   </td>
     </tr>

.. raw:: html

   <tr>
       <td>
         

registered

.. raw:: html

   </td>
       <td>
         <ul>
           <li>

None

.. raw:: html

   </li>
           <li>

insertion

.. raw:: html

   </li>
           <li>

standard

.. raw:: html

   </li>
           <li>

personal

.. raw:: html

   </li>
         </ul>
       </td>
       <td>
         

None

.. raw:: html

   </td>
       <td>
         

Einschreiben: Nein, Einwurf-Einschreiben, Standard-Einschreiben,
Einschreiben eigenhändig

.. raw:: html

   </td>
     </tr>

.. raw:: html

   <tr>
       <td>
         

payment\_slip

.. raw:: html

   </td>
       <td>
         <ul>
           <li>

None

.. raw:: html

   </li>
           <li>

national

.. raw:: html

   </li>
           <li>

sepa

.. raw:: html

   </li>
         </ul>
       </td>
       <td>
         

None

.. raw:: html

   </td>
       <td>
         

Zahlschein: Kein Zahlschein, Inlands-Zahlschein, SEPA-Zahlschein

.. raw:: html

   </td>
     </tr>
     

   </table>

Copyright
---------

`MIT
License <https://github.com/dajool/onlinebrief24/blob/master/LICENSE>`__

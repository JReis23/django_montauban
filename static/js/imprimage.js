function popup() {
    w=open("",'popup','width=400,height=200,toolbar=no,scrollbars=no,resizable=yes');
    w.document.write("<BODY>");
    w.document.write("Nom: "+document.forms[0].elements["nom"].value+"<BR><BR>");
    w.document.write("Prénom: "+document.forms[0].elements["prenom"].value+"<BR><BR>");
    w.document.write("Courriel: "+document.forms[0].elements["courriel"].value+"<BR><BR>");
    w.document.write("Message: "+document.forms[0].elements["message"].value+"<BR><BR>");
    w.document.write("</BODY>");
    w.document.close();
    w.print();
}
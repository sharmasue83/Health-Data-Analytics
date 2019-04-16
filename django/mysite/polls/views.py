from django.shortcuts import render
from django.template.response import TemplateResponse
from polls.models import Graph
import json
graph_data = ""


# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'app.html')
def bcg(request):
    
    graph = Graph('BCG')
     
    


    context = graph.get_context_data()
    try:
        
        if request.session['data'] != "BCG":
            request.session['country'] = "Afghanistan"
            request.session['graph'] = context['graph']
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"

        else:
        
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    except KeyError:
        request.session['country'] = "Afghanistan"
        request.session['graph'] = context['graph']
        context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    request.session['data'] = "BCG"

    
    context["scripts"] = """<script> console.log("Test")
var val = '"""+request.session['country']+"""';
console.log(val)

var sel = document.getElementById('country');
var opts = sel.getElementsByTagName('option');
for (var opt, j = 0; opt = opts[j]; j++) {
    if (opt.text == val) {
      sel.selectedIndex = j;
      break;
    }
 }



function GetCountry() {
  var xhr = new XMLHttpRequest();
  var dd = document.getElementById('country');
  var data = JSON.stringify({'country': dd.getElementsByTagName('option')[dd.selectedIndex].text})
  console.log(data);
  
  var url = window.location.href.replace("/BCG","")+ "/graph?country=" + dd.getElementsByTagName('option')[dd.selectedIndex].text+"&data=BCG"
  console.log(window.location.href.replace("/BCG",""))
  xhr.open("GET", url, true);
  xhr.setRequestHeader("Content-type","application/json");
  xhr.onreadystatechange = function () {
       if (xhr.readyState == 4 && xhr.status == 200) {
           // do something with response
           
            location.reload();

           console.log(xhr.responseText);
       }
  };
  
  xhr.send();
  
}
</script>"""

    context["countryList"] = graph.getCountryList()
    
    print(context)
    return TemplateResponse(request, "graph.html", context)

def DTP1(request):
    
    graph = Graph('DTP1')
     
    
    context = graph.get_context_data()
    try:
        if request.session['data'] != "DTP1":
            request.session['country'] = "Afghanistan"
            request.session['graph'] = context['graph']
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"

        else:
        
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    except KeyError:
        request.session['country'] = "Afghanistan"
        request.session['graph'] = context['graph']
        context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
        
    request.session['data'] = "DTP1"
    context["scripts"] = """<script> console.log("Test")
var val = '"""+request.session['country']+"""';
console.log(val)

var sel = document.getElementById('country');
var opts = sel.getElementsByTagName('option');
for (var opt, j = 0; opt = opts[j]; j++) {
    if (opt.text == val) {
      sel.selectedIndex = j;
      break;
    }
 }



function GetCountry() {
  var xhr = new XMLHttpRequest();
  var dd = document.getElementById('country');
  var data = JSON.stringify({'country': dd.getElementsByTagName('option')[dd.selectedIndex].text})
  console.log(data);
  
  var url = window.location.href.replace("/DTP1","")+ "/graph?country=" + dd.getElementsByTagName('option')[dd.selectedIndex].text+"&data=DTP1"
  console.log(window.location.href.replace("/DTP1",""))
  xhr.open("GET", url, true);
  xhr.setRequestHeader("Content-type","application/json");
  xhr.onreadystatechange = function () {
       if (xhr.readyState == 4 && xhr.status == 200) {
           // do something with response
           
            location.reload();

           console.log(xhr.responseText);
       }
  };
  
  xhr.send();
  
}
</script>"""

    context["countryList"] = graph.getCountryList()
    
    print(context)
    return TemplateResponse(request, "graph.html", context)
def DTP3(request):
    
    graph = Graph('DTP3')
     
    


    context = graph.get_context_data()
    try:
        
        if request.session['data'] != "DTP3":
            request.session['country'] = "Afghanistan"
            request.session['graph'] = context['graph']
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"

        else:
        
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    except KeyError:
        request.session['country'] = "Afghanistan"
        request.session['graph'] = context['graph']
        context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    request.session['data'] = "DTP3"

    
    context["scripts"] = """<script> console.log("Test")
var val = '"""+request.session['country']+"""';
console.log(val)

var sel = document.getElementById('country');
var opts = sel.getElementsByTagName('option');
for (var opt, j = 0; opt = opts[j]; j++) {
    if (opt.text == val) {
      sel.selectedIndex = j;
      break;
    }
 }



function GetCountry() {
  var xhr = new XMLHttpRequest();
  var dd = document.getElementById('country');
  var data = JSON.stringify({'country': dd.getElementsByTagName('option')[dd.selectedIndex].text})
  console.log(data);
  
  var url = window.location.href.replace("/DTP3","")+ "/graph?country=" + dd.getElementsByTagName('option')[dd.selectedIndex].text+"&data=DTP3"
  console.log(window.location.href.replace("/DTP3",""))
  xhr.open("GET", url, true);
  xhr.setRequestHeader("Content-type","application/json");
  xhr.onreadystatechange = function () {
       if (xhr.readyState == 4 && xhr.status == 200) {
           // do something with response
           
            location.reload();

           console.log(xhr.responseText);
       }
  };
  
  xhr.send();
  
}
</script>"""

    context["countryList"] = graph.getCountryList()
    
    print(context)
    return TemplateResponse(request, "graph.html", context)

def HepB3(request):
    
    graph = Graph('HepB3')
     
    


    context = graph.get_context_data()
    try:
        
        if request.session['data'] != "HepB3":
            request.session['country'] = "Afghanistan"
            request.session['graph'] = context['graph']
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"

        else:
        
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    except KeyError:
        request.session['country'] = "Afghanistan"
        request.session['graph'] = context['graph']
        context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    request.session['data'] = "HepB3"

    
    context["scripts"] = """<script> console.log("Test")
var val = '"""+request.session['country']+"""';
console.log(val)

var sel = document.getElementById('country');
var opts = sel.getElementsByTagName('option');
for (var opt, j = 0; opt = opts[j]; j++) {
    if (opt.text == val) {
      sel.selectedIndex = j;
      break;
    }
 }



function GetCountry() {
  var xhr = new XMLHttpRequest();
  var dd = document.getElementById('country');
  var data = JSON.stringify({'country': dd.getElementsByTagName('option')[dd.selectedIndex].text})
  console.log(data);
  
  var url = window.location.href.replace("/HepB3","")+ "/graph?country=" + dd.getElementsByTagName('option')[dd.selectedIndex].text+"&data=HepB3"
  console.log(window.location.href.replace("/HepB3",""))
  xhr.open("GET", url, true);
  xhr.setRequestHeader("Content-type","application/json");
  xhr.onreadystatechange = function () {
       if (xhr.readyState == 4 && xhr.status == 200) {
           // do something with response
           
            location.reload();

           console.log(xhr.responseText);
       }
  };
  
  xhr.send();
  
}
</script>"""

    context["countryList"] = graph.getCountryList()
    
    print(context)
    return TemplateResponse(request, "graph.html", context)


def HepBB(request):
    
    graph = Graph('HepBB')
     
    


    context = graph.get_context_data()
    try:
        
        if request.session['data'] != "HepBB":
            request.session['country'] = "Afghanistan"
            request.session['graph'] = context['graph']
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"

        else:
        
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    except KeyError:
        request.session['country'] = "Afghanistan"
        request.session['graph'] = context['graph']
        context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    request.session['data'] = "HepBB"

    
    context["scripts"] = """<script> console.log("Test")
var val = '"""+request.session['country']+"""';
console.log(val)

var sel = document.getElementById('country');
var opts = sel.getElementsByTagName('option');
for (var opt, j = 0; opt = opts[j]; j++) {
    if (opt.text == val) {
      sel.selectedIndex = j;
      break;
    }
 }



function GetCountry() {
  var xhr = new XMLHttpRequest();
  var dd = document.getElementById('country');
  var data = JSON.stringify({'country': dd.getElementsByTagName('option')[dd.selectedIndex].text})
  console.log(data);
  
  var url = window.location.href.replace("/HepBB","")+ "/graph?country=" + dd.getElementsByTagName('option')[dd.selectedIndex].text+"&data=HepBB"
  console.log(window.location.href.replace("/HepBB",""))
  xhr.open("GET", url, true);
  xhr.setRequestHeader("Content-type","application/json");
  xhr.onreadystatechange = function () {
       if (xhr.readyState == 4 && xhr.status == 200) {
           // do something with response
           
            location.reload();

           console.log(xhr.responseText);
       }
  };
  
  xhr.send();
  
}
</script>"""

    context["countryList"] = graph.getCountryList()
    
    print(context)
    return TemplateResponse(request, "graph.html", context)


def Hib3(request):
    
    graph = Graph('Hib3')
     
    


    context = graph.get_context_data()
    try:
        
        if request.session['data'] != "Hib3":
            request.session['country'] = "Afghanistan"
            request.session['graph'] = context['graph']
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"

        else:
        
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    except KeyError:
        request.session['country'] = "Afghanistan"
        request.session['graph'] = context['graph']
        context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    request.session['data'] = "Hib3"

    
    context["scripts"] = """<script> console.log("Test")
var val = '"""+request.session['country']+"""';
console.log(val)

var sel = document.getElementById('country');
var opts = sel.getElementsByTagName('option');
for (var opt, j = 0; opt = opts[j]; j++) {
    if (opt.text == val) {
      sel.selectedIndex = j;
      break;
    }
 }



function GetCountry() {
  var xhr = new XMLHttpRequest();
  var dd = document.getElementById('country');
  var data = JSON.stringify({'country': dd.getElementsByTagName('option')[dd.selectedIndex].text})
  console.log(data);
  
  var url = window.location.href.replace("/Hib3","")+ "/graph?country=" + dd.getElementsByTagName('option')[dd.selectedIndex].text+"&data=Hib3"
  console.log(window.location.href.replace("/Hib3",""))
  xhr.open("GET", url, true);
  xhr.setRequestHeader("Content-type","application/json");
  xhr.onreadystatechange = function () {
       if (xhr.readyState == 4 && xhr.status == 200) {
           // do something with response
           
            location.reload();

           console.log(xhr.responseText);
       }
  };
  
  xhr.send();
  
}
</script>"""

    context["countryList"] = graph.getCountryList()
    
    print(context)
    return TemplateResponse(request, "graph.html", context)

def IPV1(request):
    
    graph = Graph('IPV1')
     
    


    context = graph.get_context_data()
    try:
        
        if request.session['data'] != "IPV1":
            request.session['country'] = "Afghanistan"
            request.session['graph'] = context['graph']
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"

        else:
        
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    except KeyError:
        request.session['country'] = "Afghanistan"
        request.session['graph'] = context['graph']
        context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    request.session['data'] = "IPV1"

    
    context["scripts"] = """<script> console.log("Test")
var val = '"""+request.session['country']+"""';
console.log(val)

var sel = document.getElementById('country');
var opts = sel.getElementsByTagName('option');
for (var opt, j = 0; opt = opts[j]; j++) {
    if (opt.text == val) {
      sel.selectedIndex = j;
      break;
    }
 }



function GetCountry() {
  var xhr = new XMLHttpRequest();
  var dd = document.getElementById('country');
  var data = JSON.stringify({'country': dd.getElementsByTagName('option')[dd.selectedIndex].text})
  console.log(data);
  
  var url = window.location.href.replace("/IPV1","")+ "/graph?country=" + dd.getElementsByTagName('option')[dd.selectedIndex].text+"&data=IPV1"
  console.log(window.location.href.replace("/IPV1",""))
  xhr.open("GET", url, true);
  xhr.setRequestHeader("Content-type","application/json");
  xhr.onreadystatechange = function () {
       if (xhr.readyState == 4 && xhr.status == 200) {
           // do something with response
           
            location.reload();

           console.log(xhr.responseText);
       }
  };
  
  xhr.send();
  
}
</script>"""

    context["countryList"] = graph.getCountryList()
    
    print(context)
    return TemplateResponse(request, "graph.html", context)

def MCV1(request):
    
    graph = Graph('MCV1')
     
    


    context = graph.get_context_data()
    try:
        
        if request.session['data'] != "MCV1":
            request.session['country'] = "Afghanistan"
            request.session['graph'] = context['graph']
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"

        else:
        
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    except KeyError:
        request.session['country'] = "Afghanistan"
        request.session['graph'] = context['graph']
        context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    request.session['data'] = "MCV1"

    
    context["scripts"] = """<script> console.log("Test")
var val = '"""+request.session['country']+"""';
console.log(val)

var sel = document.getElementById('country');
var opts = sel.getElementsByTagName('option');
for (var opt, j = 0; opt = opts[j]; j++) {
    if (opt.text == val) {
      sel.selectedIndex = j;
      break;
    }
 }



function GetCountry() {
  var xhr = new XMLHttpRequest();
  var dd = document.getElementById('country');
  var data = JSON.stringify({'country': dd.getElementsByTagName('option')[dd.selectedIndex].text})
  console.log(data);
  
  var url = window.location.href.replace("/MCV1","")+ "/graph?country=" + dd.getElementsByTagName('option')[dd.selectedIndex].text+"&data=MCV1"
  console.log(window.location.href.replace("/MCV1",""))
  xhr.open("GET", url, true);
  xhr.setRequestHeader("Content-type","application/json");
  xhr.onreadystatechange = function () {
       if (xhr.readyState == 4 && xhr.status == 200) {
           // do something with response
           
            location.reload();

           console.log(xhr.responseText);
       }
  };
  
  xhr.send();
  
}
</script>"""

    context["countryList"] = graph.getCountryList()
    
    print(context)
    return TemplateResponse(request, "graph.html", context)


def MCV2(request):
    
    graph = Graph('MCV2')
     
    


    context = graph.get_context_data()
    try:
        
        if request.session['data'] != "MCV2":
            request.session['country'] = "Afghanistan"
            request.session['graph'] = context['graph']
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"

        else:
        
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    except KeyError:
        request.session['country'] = "Afghanistan"
        request.session['graph'] = context['graph']
        context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    request.session['data'] = "MCV2"

    
    context["scripts"] = """<script> console.log("Test")
var val = '"""+request.session['country']+"""';
console.log(val)

var sel = document.getElementById('country');
var opts = sel.getElementsByTagName('option');
for (var opt, j = 0; opt = opts[j]; j++) {
    if (opt.text == val) {
      sel.selectedIndex = j;
      break;
    }
 }



function GetCountry() {
  var xhr = new XMLHttpRequest();
  var dd = document.getElementById('country');
  var data = JSON.stringify({'country': dd.getElementsByTagName('option')[dd.selectedIndex].text})
  console.log(data);
  
  var url = window.location.href.replace("/MCV2","")+ "/graph?country=" + dd.getElementsByTagName('option')[dd.selectedIndex].text+"&data=MCV2"
  console.log(window.location.href.replace("/MCV2",""))
  xhr.open("GET", url, true);
  xhr.setRequestHeader("Content-type","application/json");
  xhr.onreadystatechange = function () {
       if (xhr.readyState == 4 && xhr.status == 200) {
           // do something with response
           
            location.reload();

           console.log(xhr.responseText);
       }
  };
  
  xhr.send();
  
}
</script>"""

    context["countryList"] = graph.getCountryList()
    
    print(context)
    return TemplateResponse(request, "graph.html", context)


def PCV3(request):
    
    graph = Graph('PCV3')
     
    


    context = graph.get_context_data()
    try:
        
        if request.session['data'] != "PCV3":
            request.session['country'] = "Afghanistan"
            request.session['graph'] = context['graph']
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"

        else:
        
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    except KeyError:
        request.session['country'] = "Afghanistan"
        request.session['graph'] = context['graph']
        context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    request.session['data'] = "PCV3"

    
    context["scripts"] = """<script> console.log("Test")
var val = '"""+request.session['country']+"""';
console.log(val)

var sel = document.getElementById('country');
var opts = sel.getElementsByTagName('option');
for (var opt, j = 0; opt = opts[j]; j++) {
    if (opt.text == val) {
      sel.selectedIndex = j;
      break;
    }
 }



function GetCountry() {
  var xhr = new XMLHttpRequest();
  var dd = document.getElementById('country');
  var data = JSON.stringify({'country': dd.getElementsByTagName('option')[dd.selectedIndex].text})
  console.log(data);
  
  var url = window.location.href.replace("/PCV3","")+ "/graph?country=" + dd.getElementsByTagName('option')[dd.selectedIndex].text+"&data=PCV3"
  console.log(window.location.href.replace("/PCV3",""))
  xhr.open("GET", url, true);
  xhr.setRequestHeader("Content-type","application/json");
  xhr.onreadystatechange = function () {
       if (xhr.readyState == 4 && xhr.status == 200) {
           // do something with response
           
            location.reload();

           console.log(xhr.responseText);
       }
  };
  
  xhr.send();
  
}
</script>"""

    context["countryList"] = graph.getCountryList()
    
    print(context)
    return TemplateResponse(request, "graph.html", context)

def Pol3(request):
    
    graph = Graph('Pol3')
     
    


    context = graph.get_context_data()
    try:
        
        if request.session['data'] != "Pol3":
            request.session['country'] = "Afghanistan"
            request.session['graph'] = context['graph']
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"

        else:
        
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    except KeyError:
        request.session['country'] = "Afghanistan"
        request.session['graph'] = context['graph']
        context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    request.session['data'] = "Pol3"

    
    context["scripts"] = """<script> console.log("Test")
var val = '"""+request.session['country']+"""';
console.log(val)

var sel = document.getElementById('country');
var opts = sel.getElementsByTagName('option');
for (var opt, j = 0; opt = opts[j]; j++) {
    if (opt.text == val) {
      sel.selectedIndex = j;
      break;
    }
 }



function GetCountry() {
  var xhr = new XMLHttpRequest();
  var dd = document.getElementById('country');
  var data = JSON.stringify({'country': dd.getElementsByTagName('option')[dd.selectedIndex].text})
  console.log(data);
  
  var url = window.location.href.replace("/Pol3","")+ "/graph?country=" + dd.getElementsByTagName('option')[dd.selectedIndex].text+"&data=Pol3"
  console.log(window.location.href.replace("/Pol3",""))
  xhr.open("GET", url, true);
  xhr.setRequestHeader("Content-type","application/json");
  xhr.onreadystatechange = function () {
       if (xhr.readyState == 4 && xhr.status == 200) {
           // do something with response
           
            location.reload();

           console.log(xhr.responseText);
       }
  };
  
  xhr.send();
  
}
</script>"""

    context["countryList"] = graph.getCountryList()
    
    print(context)
    return TemplateResponse(request, "graph.html", context)



def ROTAC(request):
    
    graph = Graph('ROTAC')
     
    


    context = graph.get_context_data()
    try:
        
        if request.session['data'] != "ROTAC":
            request.session['country'] = "Afghanistan"
            request.session['graph'] = context['graph']
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"

        else:
        
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    except KeyError:
        request.session['country'] = "Afghanistan"
        request.session['graph'] = context['graph']
        context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    request.session['data'] = "ROTAC"

    
    context["scripts"] = """<script> console.log("Test")
var val = '"""+request.session['country']+"""';
console.log(val)

var sel = document.getElementById('country');
var opts = sel.getElementsByTagName('option');
for (var opt, j = 0; opt = opts[j]; j++) {
    if (opt.text == val) {
      sel.selectedIndex = j;
      break;
    }
 }



function GetCountry() {
  var xhr = new XMLHttpRequest();
  var dd = document.getElementById('country');
  var data = JSON.stringify({'country': dd.getElementsByTagName('option')[dd.selectedIndex].text})
  console.log(data);
  
  var url = window.location.href.replace("/ROTAC","")+ "/graph?country=" + dd.getElementsByTagName('option')[dd.selectedIndex].text+"&data=ROTAC"
  console.log(window.location.href.replace("/ROTAC",""))
  xhr.open("GET", url, true);
  xhr.setRequestHeader("Content-type","application/json");
  xhr.onreadystatechange = function () {
       if (xhr.readyState == 4 && xhr.status == 200) {
           // do something with response
           
            location.reload();

           console.log(xhr.responseText);
       }
  };
  
  xhr.send();
  
}
</script>"""

    context["countryList"] = graph.getCountryList()
    
    print(context)
    return TemplateResponse(request, "graph.html", context)

def YFV(request):
    
    graph = Graph('YFV')
     
    


    context = graph.get_context_data(country='Angola')
    try:
        
        if request.session['data'] != "YFV":
            request.session['country'] = "Angola"
            request.session['graph'] = context['graph']
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"

        else:
        
            context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    except KeyError:
        request.session['country'] = "Angola"
        request.session['graph'] = context['graph']
        context['graph'] = "<div id='graph'>" + request.session['graph'] + "</div>"
    request.session['data'] = "YFV"

    
    context["scripts"] = """<script> console.log("Test")
var val = '"""+request.session['country']+"""';
console.log(val)

var sel = document.getElementById('country');
var opts = sel.getElementsByTagName('option');
for (var opt, j = 0; opt = opts[j]; j++) {
    if (opt.text == val) {
      sel.selectedIndex = j;
      break;
    }
 }



function GetCountry() {
  var xhr = new XMLHttpRequest();
  var dd = document.getElementById('country');
  var data = JSON.stringify({'country': dd.getElementsByTagName('option')[dd.selectedIndex].text})
  console.log(data);
  
  var url = window.location.href.replace("/YFV","")+ "/graph?country=" + dd.getElementsByTagName('option')[dd.selectedIndex].text+"&data=YFV"
  console.log(window.location.href.replace("/YFV",""))
  xhr.open("GET", url, true);
  xhr.setRequestHeader("Content-type","application/json");
  xhr.onreadystatechange = function () {
       if (xhr.readyState == 4 && xhr.status == 200) {
           // do something with response
           
            location.reload();

           console.log(xhr.responseText);
       }
  };
  
  xhr.send();
  
}
</script>"""

    context["countryList"] = graph.getCountryList()
    
    print(context)
    return TemplateResponse(request, "graph.html", context)



def graph(request):
    print(request.GET.get('country', ''))
    graphData = request.GET.get('data','')
    request.session['country'] = request.GET.get('country', '')
    request.session['graph'] = Graph(graphData).get_context_data(request.GET.get('country', ''))['graph']
    return HttpResponse("ok")

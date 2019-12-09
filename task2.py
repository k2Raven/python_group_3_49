$.ajax({
    url: 'http://localhost:8000/api/v2/login/',
    method: 'post',
    data: JSON.stringify({username: 'admin', password: 'admin'}),
    dataType: 'json',
    contentType: 'application/json',
    success: function(response, status){localStorage.setItem('tokenAdmin', response.token);},
    error: function(response, status){console.log(response);}
});

$.ajax({
    url: 'http://localhost:8000/api/v2/projects/',
    method: 'get',
    dataType: 'json',
    contentType: 'application/json',
    success: function(response, status){console.log(response);},
    error: function(response, status){console.log(response);}
});

$.ajax({
    url: 'http://localhost:8000/api/v2/tasks/',
    method: 'get',
    dataType: 'json',
    contentType: 'application/json',
    success: function(response, status){console.log(response);},
    error: function(response, status){console.log(response);}
});

$.ajax({
    url: 'http://localhost:8000/api/v2/projects/2',
    method: 'get',
    dataType: 'json',
    contentType: 'application/json',
    success: function(response, status){console.log(response.tasks);},
    error: function(response, status){console.log(response);}
});

$.ajax({
    url: 'http://localhost:8000/api/v2/tasks/',
    method: 'post',
    headers: {'Authorization': 'Token ' + localStorage.getItem('tokenAdmin')},
    data: JSON.stringify({project: 2, summary: '12345q', description: '12345q', status: 2, types: 2}),
    dataType: 'json',
    contentType: 'application/json',
    success: function(response, status){console.log(response);},
    error: function(response, status){console.log(response);}
});

$.ajax({
    url: 'http://localhost:8000/api/v2/tasks/13',
    method: 'delete',
    headers: {'Authorization': 'Token ' + localStorage.getItem('tokenAdmin')},
    dataType: 'json',
    contentType: 'application/json',
    success: function(response, status){console.log(response);},
    error: function(response, status){console.log(response);}
});
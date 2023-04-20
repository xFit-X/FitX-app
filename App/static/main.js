
async function getUserData(){
    const response = await fetch('/api/users');
    return response.json();
}

function loadTable(users){
    const table = document.querySelector('#result');
    for(let user of users){
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
        </tr>`;
    }
}

async function main(){
    const users = await getUserData();
    loadTable(users);
}

document.addEventListener('DOMContentLoaded', function() {
    var tabs = document.querySelectorAll('.tabs');
    M.Tabs.init(tabs);
  });
  
          
var buttons = document.querySelectorAll('.modal-trigger');
for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function() {
        var workoutId = this.getAttribute('data-workout-id');
        var workoutName = this.getAttribute('data-workout-name');
        document.getElementById('modal-title').innerHTML = workoutName;
        document.getElementById('workoutId').value = workoutId;
    });
}

const navbarSearch = document.querySelector('#navbar-search');
const navbarClearIcon = document.querySelector('.clear-icon');
navbarSearch.addEventListener('input', () => {
    if (navbarSearch.value !== '') {
        navbarClearIcon.style.display = 'block';
    } else {
        navbarClearIcon.style.display = 'none';
    }
});
navbarClearIcon.addEventListener('click', () => {
navbarSearch.value = '';
navbarClearIcon.style.display = 'none';
});

var buttons = document.querySelectorAll('.modal-trigger2');
for (var i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener('click', function() {
    var workoutId = this.getAttribute('data-pworkout-id');
    var workoutName = this.getAttribute('data-pworkout-name');
    document.getElementById('modal-title2').innerHTML = workoutName;
    document.getElementById('pwid').value = workoutId;
  });
}


main();
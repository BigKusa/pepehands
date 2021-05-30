const gradebook = {
    'A': 4.00, 'A-': 3.70, 'B+': 3.33, 'B': 3.00, 'B-': 2.70,
    'C+': 2.30, 'C': 2.00, 'C-': 1.70, 'D+': 1.30, 'D': 1.00, 'D-': 0.7, 'F': 0
};
const keys = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F',];
var count = 0;
const Form = document.getElementById('form');
Form.addEventListener('submit', (event) => {
    event.preventDefault();
    grades = Form.grades.value.trim();
    weights = Form.weights.value.trim();
    Check();
});

function Check() {
    if (grades.length==0){
        alert("Grades were not inserted");
        return;
    }
    if (weights.length==0){
        alert("Credit hours were not inserted");
        return;
    }
    grades = grades.split(" ");
    weights = weights.split(" ");
    for (var i = 0; i < grades.length; i++) {
        if (keys.indexOf(grades[i]) !== -1) {
            count = count + 1;
            grades[i] = gradebook[grades[i]];
        } else {
            alert("Wrong input for grades");
            count = 0;
            return;
        }
    };
    count = 0;
    for (var i = 0; i < weights.length; i++) {
        if (isNaN(weights[i])) {
            alert("Wrong input for credit hours");
            return;
        } else {
            count = count + 1;
            weights[i] = +weights[i];
        }
    };
    if (count !== grades.length) {
        alert("Numbers of grades and credit hours are not similar");
        return;
    }
    var total = 0;
    totalweights = 0;
    for (var i = 0; i < grades.length; i++) {
        total = total + grades[i] * weights[i];
        totalweights = totalweights + weights[i];
    };
    var gpa = total / totalweights;
    gpa=Math.round(gpa * 100) / 100;
    document.getElementById('gpa').innerText = "Your GPA: " + gpa;
}

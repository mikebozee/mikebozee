var jobTitles = ["Software Development Engineer", "Web Development Engineer", "Web Application Developer"];

function rotateJobTitle() {
  var jt = $("#job-title-rotate").data("jobTitle") || 0;
  $("#job-title-rotate").data("jobTitle", jt == jobTitles.length -1 ? 0 : jt + 1).text(jobTitles[jt]).fadeIn()
              .delay(3000).fadeOut(800, rotateJobTitle);
}
$(rotateJobTitle);







function moveSectionToTop(section) {
	var sectionId = section.getAttribute('data-section')
	var sectionElement = '#' + sectionId;
	$(sectionElement).prependTo('#sections');
}

// function moveSectionToTop(animal) {
//     var animalType = animal.getAttribute("data-section");
//     alert("The " + animal.innerHTML + " is a " + animalType + ".");
// }
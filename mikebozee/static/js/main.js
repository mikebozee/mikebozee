
// Rotate through intended job titles text.
var jobTitles = ["Software Development Engineer", "Web Development Engineer", "Web Application Developer"];

function rotateJobTitle() {
  var jt = $("#job-title-rotate").data("jobTitle") || 0;
  $("#job-title-rotate").data("jobTitle", jt == jobTitles.length -1 ? 0 : jt + 1).text(jobTitles[jt]).fadeIn()
              .delay(3000).fadeOut(800, rotateJobTitle);
}
$(rotateJobTitle);






// Clicking onnav item moves the related section to top.
function moveSectionToTop(section) {
	var sectionId = section.getAttribute('data-section')
	var sectionElement = '#' + sectionId;
	$(sectionElement).prependTo('#sections');
}
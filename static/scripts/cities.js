var state_arr = new Array("Northern", "NorthWestern", "Western", "NorthCentral", "Central", "Sabaragamuwa", "Eastern", "Uva", "Southern	");

var s_a = new Array();
s_a[0]="";
s_a[1]="Jaffna | Kilinochchi | Mannar | Mullaitivu | Vavuniya";
s_a[2]="Puttalam | Kurunegala";
s_a[3]="Gampaha | Colombo | Kalutara";
s_a[4]="Anuradhapura | Polonnaruwa";
s_a[5]=" Matale | Kandy | Nuwara Eliya";
s_a[6]="Kegalle | Ratnapura ";
s_a[7]="Trincomalee | Batticaloa | Ampara ";
s_a[8]="Badulla | Monaragala ";
s_a[9]="Hambantota | Matara | Galle ";


function print_state(state_id){
	// given the id of the <select> tag as function argument, it inserts <option> tags
	var option_str = document.getElementById(state_id);
	option_str.length=0;
	option_str.options[0] = new Option('Select State','');
	option_str.selectedIndex = 0;
	for (var i=0; i<state_arr.length; i++) {
		option_str.options[option_str.length] = new Option(state_arr[i],state_arr[i]);
	}
}

function print_city(city_id, city_index){
	var option_str = document.getElementById(city_id);
	option_str.length=0;	// Fixed by Julian Woods
	option_str.options[0] = new Option('Select City','');
	option_str.selectedIndex = 0;
	var city_arr = s_a[city_index].split("|");
	for (var i=0; i<city_arr.length; i++) {
		option_str.options[option_str.length] = new Option(city_arr[i],city_arr[i]);
	}
}

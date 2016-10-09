difference() {
cylinder(d=75,h=35,$fn=50);
    translate([0,0,25])cylinder(d=50,h=10.1,$fn=50);
%    translate([0,0,25])cylinder(d=55,h=5,$fn=50);
    translate([0,0,15-0.1])cube([60,35,30], center=true);
    translate([10,0,5-0.1])cube([60,15,10],center=true);
}
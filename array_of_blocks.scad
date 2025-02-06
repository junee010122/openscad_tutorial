// OpenSCAD script to generate an array of square blocks
module block() {
  cube([55, 55, 300], center = true);
}
translate([0, 0, 0])
{
translate([0, 0, 150.0]) block();
translate([0, 455, 150.0]) block();
translate([0, 910, 150.0]) block();
translate([0, 1365, 150.0]) block();
translate([0, 1820, 150.0]) block();
translate([0, 2275, 150.0]) block();
translate([0, 2730, 150.0]) block();
translate([455, 0, 150.0]) block();
translate([455, 455, 150.0]) block();
translate([455, 910, 150.0]) block();
translate([455, 1365, 150.0]) block();
translate([455, 1820, 150.0]) block();
translate([455, 2275, 150.0]) block();
translate([455, 2730, 150.0]) block();
translate([910, 0, 150.0]) block();
translate([910, 455, 150.0]) block();
translate([910, 910, 150.0]) block();
translate([910, 1365, 150.0]) block();
translate([910, 1820, 150.0]) block();
translate([910, 2275, 150.0]) block();
translate([910, 2730, 150.0]) block();
translate([1365, 0, 150.0]) block();
translate([1365, 455, 150.0]) block();
translate([1365, 910, 150.0]) block();
translate([1365, 1365, 150.0]) block();
translate([1365, 1820, 150.0]) block();
translate([1365, 2275, 150.0]) block();
translate([1365, 2730, 150.0]) block();
translate([1820, 0, 150.0]) block();
translate([1820, 455, 150.0]) block();
translate([1820, 910, 150.0]) block();
translate([1820, 1365, 150.0]) block();
translate([1820, 1820, 150.0]) block();
translate([1820, 2275, 150.0]) block();
translate([1820, 2730, 150.0]) block();
translate([2275, 0, 150.0]) block();
translate([2275, 455, 150.0]) block();
translate([2275, 910, 150.0]) block();
translate([2275, 1365, 150.0]) block();
translate([2275, 1820, 150.0]) block();
translate([2275, 2275, 150.0]) block();
translate([2275, 2730, 150.0]) block();
translate([2730, 0, 150.0]) block();
translate([2730, 455, 150.0]) block();
translate([2730, 910, 150.0]) block();
translate([2730, 1365, 150.0]) block();
translate([2730, 1820, 150.0]) block();
translate([2730, 2275, 150.0]) block();
translate([2730, 2730, 150.0]) block();
}

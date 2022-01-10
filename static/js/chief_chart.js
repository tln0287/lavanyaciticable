/**
 * ---------------------------------------
 * This demo was created using amCharts 4.
 *
 * For more information visit:
 * https://www.amcharts.com/
 *
 * Documentation is available at:
 * https://www.amcharts.com/docs/v4/
 * ---------------------------------------
 */

// Themes begin
am4core.useTheme(am4themes_animated);
// Themes end

// Create chart instance
var chart = am4core.create("chart11", am4charts.PieChart);

// Add data
chart.data ={{chief_chart1 | safe}};

// Add and configure Series
var pieSeries = chart.series.push(new am4charts.PieSeries());
pieSeries.dataFields.value = "count";
pieSeries.dataFields.category = "version";
pieSeries.innerRadius = am4core.percent(50);
pieSeries.ticks.template.disabled = true;
pieSeries.labels.template.disabled = true;

var rgm = new am4core.RadialGradientModifier();
rgm.brightnesses.push(-0.8, -0.8, -0.5, 0, - 0.5);
pieSeries.slices.template.fillModifier = rgm;
pieSeries.slices.template.strokeModifier = rgm;
pieSeries.slices.template.strokeOpacity = 0.4;
pieSeries.slices.template.strokeWidth = 0;

chart.legend = new am4charts.Legend();
chart.legend.position = "right";
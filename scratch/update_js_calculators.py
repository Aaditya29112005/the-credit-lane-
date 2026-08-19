import os

# Update build.py JS logic
build_py = "/Users/aadityamohansamadhiya/the credit lane/build.py"
with open(build_py, "r", encoding="utf-8") as f:
    code = f.read()

slider_fill_func = """    function updateSliderFill(slider) {
      if (!slider) return;
      var min = parseFloat(slider.min) || 0;
      var max = parseFloat(slider.max) || 100;
      var val = parseFloat(slider.value) || 0;
      var pct = max > min ? ((val - min) / (max - min)) * 100 : 50;
      slider.style.background = 'linear-gradient(to right, #C89B3C 0%, #C89B3C ' + pct + '%, #E2DDD5 ' + pct + '%, #E2DDD5 100%)';
    }

    function updateEmiCalc() {"""

code = code.replace("    function updateEmiCalc() {", slider_fill_func)

# Add updateSliderFill inside calculator functions
code = code.replace(
    '      if (!pInput || !rInput || !yInput) return;\n',
    '      if (!pInput || !rInput || !yInput) return;\n      updateSliderFill(pInput);\n      updateSliderFill(rInput);\n      updateSliderFill(yInput);\n'
)
code = code.replace(
    '      if (!valInput || !advInput || !daysInput) return;\n',
    '      if (!valInput || !advInput || !daysInput) return;\n      updateSliderFill(valInput);\n      updateSliderFill(advInput);\n      updateSliderFill(daysInput);\n'
)
code = code.replace(
    '      if (!duesInput || !setPctInput || !tokPctInput) return;\n',
    '      if (!duesInput || !setPctInput || !tokPctInput) return;\n      updateSliderFill(duesInput);\n      updateSliderFill(setPctInput);\n      updateSliderFill(tokPctInput);\n'
)
code = code.replace(
    '      if (!raiseInput || !preInput) return;\n      var raise',
    '      if (!raiseInput || !preInput) return;\n      updateSliderFill(raiseInput);\n      updateSliderFill(preInput);\n      var raise'
)
code = code.replace(
    '      if (!issueInput || !preInput) return;\n      var fresh',
    '      if (!issueInput || !preInput) return;\n      updateSliderFill(issueInput);\n      updateSliderFill(preInput);\n      var fresh'
)
code = code.replace(
    '      if (!ebitdaInput || !multLoInput || !multHiInput) return;\n',
    '      if (!ebitdaInput || !multLoInput || !multHiInput) return;\n      updateSliderFill(ebitdaInput);\n      updateSliderFill(multLoInput);\n      updateSliderFill(multHiInput);\n'
)
code = code.replace(
    '      if (!costInput || !rateInput) return;\n',
    '      if (!costInput || !rateInput) return;\n      updateSliderFill(costInput);\n      updateSliderFill(rateInput);\n'
)

with open(build_py, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated build.py with updateSliderFill.")

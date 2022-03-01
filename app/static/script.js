function getData() {
    Temp = document.getElementById("Temp").value
    material = document.getElementById("material").value
    console.log(material)
    oldBody = document.getElementById("tableBody")
    $.get("https://brians-flask.herokuapp.com/data", { "Temp": Temp, "material": material }, function (data, textStatus, jqXHR) {
        console.log(data)
        const keys = Object.keys(data)
        tableBody = document.createElement("tbody")
        tableBody.className = "bg-white divide-y divide-gray-200 dark:bg-gray-800 dark:divide-gray-700"
        tableBody.id = "tableBody"
        keys.forEach((key, index) => {
            console.log(`${key}: ${data[key]}`);
            [val, power] = smartRound(data[key])
            str = val

            let tr = addRow(key, str, power)
            tableBody.append(tr)
        });
        oldBody.parentNode.replaceChild(tableBody, oldBody)

    });
}


function addValue(value, power) {
    let data = document.createElement("td")
    data.className = "py-4 px-6 text-sm font-medium text-gray-500 text-center whitespace-nowrap dark:text-white"
    data.append(value)
    if (power != 1) {
        exponent = document.createElement("sup")
        exponent.innerHTML = power
        data.append(" · 10")
        data.append(exponent)
    }
    return (data)
}

function addRow(prop, value, power) {
    let row = document.createElement("tr")
    row.className = "hover:bg-gray-100 dark:hover:bg-gray-700"
    let d1 = document.createElement("td")
    d1.className = "py-4 px-6 text-sm font-medium text-gray-900 text-center whitespace-nowrap dark:text-white"

    let d2 = addValue(value, power)


    let d3 = document.createElement("td")
    d3.href = "#"
    d3.append("Copy")
    d3.className = "py-4 px-6 text-sm font-medium text-right whitespace-nowrap text-blue-600 dark:text-blue-500 hover:underline"


    d1.append(prop)
    row.appendChild(d1)
    row.appendChild(d2)
    row.appendChild(d3)
    return (row)
}

function smartRound(num) {
    smallNum = Math.abs(num)

    if (smallNum >= 1000) {
        power = Math.floor(Math.log10(smallNum))
        power = power - power % 3
        smallNum = smallNum / (10 ** power)
        smallNum = Math.round((smallNum + Number.EPSILON) * 100) / 100
    } else if (smallNum < 0.01) {
        power = Math.abs(Math.floor(Math.log10(smallNum)))
        power = power - 1
        power = power - power % 3
        smallNum = (smallNum * 1000 * (10 ** power))
        smallNum = Math.round((smallNum + Number.EPSILON) * 100) / 100
        power = -(power + 3)

    }
    else {
        smallNum = Math.round((smallNum + Number.EPSILON) * 100) / 100
        power = 1
    }
    if (num < 0) {
        smallNum = smallNum * -1
    }
    return ([smallNum, power])
}


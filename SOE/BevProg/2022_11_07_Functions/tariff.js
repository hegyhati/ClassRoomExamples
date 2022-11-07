function input_nonnegative_number(message) { // Sarah
    number = Number(prompt(message))
    while (number < 0) {
        number = Number(prompt("Nemnegativat adj meg."))
    }
    return number
}

function monthly_cost(tariff_cost, usage) { // Alexa
    return tariff_cost[0] * usage[0] + tariff_cost[1] * usage[1]
}

function input_tariff_costs(tariff_name) { //Attila
    minute_cost = input_nonnegative_number(`Mennyi a ${tariff_name} tarifa percdija?`)
    sms_cost = input_nonnegative_number(`Mennyi a ${tariff_name} tarifa sms dija?`)
    return [minute_cost, sms_cost]
}

function input_monthly_usage(month) { //Anna
    minute_usage = input_nonnegative_number(`Mennyi percet telefonalt Mate ${month} honapban?`)
    sms_usage = input_nonnegative_number(`Mennyi sms-t kuldott Mate ${month} honapban?`)
    return [minute_usage, sms_usage]
}

tariff1 = input_tariff_costs("elso")
tariff2 = input_tariff_costs("masodik")

january = input_monthly_usage("januar")

cost1 = monthly_cost(tariff1, january)
cost2 = monthly_cost(tariff2, january)

if (cost1 < cost2) {
    alert("Az elso tarififa a jobb.")
} else {
    alert("A masodik tarifa a jobb.")
}
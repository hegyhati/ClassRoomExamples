import ttura

jd2019=ttura.Calendar("John_Doe_2019")

print(f"Participated in {jd2019.total_activity_count()} activities.")
for type in ["hiking","cycling"]:
    print(f" - {jd2019.total_distance(type)} km of {type}")

jd2019.generate_statistics("stats.png")
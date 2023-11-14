import pathlib, pandas
import plt

folder = str(pathlib.Path(__file__).parent.resolve())

### IR LED driver
data = pandas.read_csv(folder + "/data/measurement.csv", comment='#')

plt.plt(
    [
        data["V_in"],
        data["V_in"],
        data["V_in"]
    ],
    [
        data["I_in"],
        data["I_out"],
        data["I_des"]
    ],
    [
        "Input Current",
        "Output Current",
        "Designed Current"
    ],
    "V_in [V]",
    "I [mA]",
    (0, 800),
    folder + "/plots/measurement.png"
)

plt.plt(
    [
        data["V_in"]
    ],
    [
        (data["I_out"] * data["V_out"]) / (data["I_in"] * data["V_in"])
    ],
    [
        ""
    ],
    "V_in [V]",
    "efficiency",
    (0.8, 1),
    folder + "/plots/measurement_eff.png"
)

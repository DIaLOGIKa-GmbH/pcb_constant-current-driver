import pathlib, pandas
import plt

folder = str(pathlib.Path(__file__).parent.resolve())

### LED driver
data_lm3404 = pandas.read_csv(folder + "/data/measurement_lm3404.csv", comment='#')
data_al8860 = pandas.read_csv(folder + "/data/measurement_al8860.csv", comment='#')

### LM3404 ###

plt.plt(
    [
        data_lm3404["V_in"],
        data_lm3404["V_in"]
    ],
    [
        data_lm3404["I_in"],
        data_lm3404["I_out"]
    ],
    [
        "Input Current",
        "Output Current"
    ],
    "V_in [V]",
    "I [mA]",
    (0, 650),
    folder + "/plots/measurement_lm3404.png"
)

plt.plt(
    [
        data_lm3404["V_in"]
    ],
    [
        (data_lm3404["I_out"] * data_lm3404["V_out"]) / (data_lm3404["I_in"] * data_lm3404["V_in"])
    ],
    [
        ""
    ],
    "V_in [V]",
    "efficiency",
    (0.8, 1),
    folder + "/plots/measurement_lm3404_eff.png"
)

### AL8860 ###

plt.plt(
    [
        data_al8860["V_in"],
        data_al8860["V_in"],
        data_al8860["V_in"]
    ],
    [
        data_al8860["I_in"],
        data_al8860["I_out"],
        data_al8860["I_des"]
    ],
    [
        "Input Current",
        "Output Current",
        "Designed Current"
    ],
    "V_in [V]",
    "I [mA]",
    (0, 800),
    folder + "/plots/measurement_al8860.png"
)

plt.plt(
    [
        data_al8860["V_in"]
    ],
    [
        (data_al8860["I_out"] * data_al8860["V_out"]) / (data_al8860["I_in"] * data_al8860["V_in"])
    ],
    [
        ""
    ],
    "V_in [V]",
    "efficiency",
    (0.8, 1),
    folder + "/plots/measurement_al8860_eff.png"
)

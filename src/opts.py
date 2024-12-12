"""Module defining data, model and plotting options."""

import pathlib

import numpy as np


def get_opts():
    """Return a dictionary of data, model and plotting options."""
    year_range = [2030, 2100]  # inclusive
    location_default = "London"
    locations_additional = ["Paris", "Los Angeles", "Istanbul", "Cape Town"]
    epi_model_name_default = "mordecai_ae_albopictus_niche"
    epi_model_species_default = "Ae. albopictus"
    epi_model_name_additional = "mordecai_ae_aegypti_niche"
    epi_model_species_additional = "Ae. aegypti"
    uncertainty_level = 90
    polyfit_degree = 3
    plot_opts_base = {
        "title": "",
        "xlim": (year_range[0], year_range[1]),
        "xticks": np.arange(year_range[0], year_range[1] + 1, 10),
        "xlabel": "",
        "legend_position": "top_left",
    }
    plot_opts_clim = {
        **plot_opts_base,
        "ylim": (9, 18),
        "yticks": np.arange(9, 19, 3),
        "ylabel": "Annual mean temperature (°C)",
    }
    plot_opts_epi = {
        **plot_opts_base,
        "ylim": (0, 7),
        "yticks": np.arange(8),
        "ylabel": "Months suitable for transmission",
    }
    data_base_dir = pathlib.Path(__file__).parents[1] / "data"
    figure_dir = pathlib.Path(__file__).parents[1] / "figures"
    opts = {
        "year_range": year_range,
        "location_default": location_default,
        "locations_additional": locations_additional,
        "epi_model_name_default": epi_model_name_default,
        "epi_model_species_default": epi_model_species_default,
        "epi_model_name_additional": epi_model_name_additional,
        "epi_model_species_additional": epi_model_species_additional,
        "uncertainty_level": uncertainty_level,
        "polyfit_degree": polyfit_degree,
        "plot_opts_clim": plot_opts_clim,
        "plot_opts_epi": plot_opts_epi,
        "data_base_dir": data_base_dir,
        "figure_dir": figure_dir,
    }
    return opts

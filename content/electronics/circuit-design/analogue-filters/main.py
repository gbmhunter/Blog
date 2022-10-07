import csv
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib.ticker as ticker

def main():
    # create_freq_response_plot()

    # create_sallen_key_response_plot(Path('low-pass-sallen-key'))
    # create_sallen_key_response_plot(Path('low-pass-sallen-key-chebyshev-3db'))
    # create_sallen_key_response_plot(Path('low-pass-sallen-key-butterworth'))

    # # Low-Pass Filter Comparison Plots
    # config = [
    #     {
    #         'data_path': Path('low-pass-sallen-key-chebyshev-3db/sim-results.csv'),
    #         'legend': 'Chebyshev 3dB',
    #     },
    #     {
    #         'data_path': Path('low-pass-sallen-key-butterworth/sim-results.csv'),
    #         'legend': 'Butterworth',
    #     },
    #     {
    #         'data_path': Path('low-pass-sallen-key-bessel/sim-results.csv'),
    #         'legend': 'Bessel',
    #     },
    # ]
    # create_low_pass_filter_comparison_plots(config)

    # # Create plot showing Sallen-Key gain rise due to non-zero op-amp output impedance
    # create_sallen_key_bode_plot_showing_gain_rise()

    create_butterworth_table()

def parse_row(data_in):
    out = np.array(data_in)
    out = out[1:-1]
    out = out.astype(float)
    return out

def get_freq_mag_phase(csv_file_path):
    with csv_file_path.open() as f:
        reader = csv.reader(f, delimiter=';')
        rows = [ row for row in reader ]
        freq_data = parse_row(rows[0])
        vout_mag_data = parse_row(rows[1])
        vout_phase_data = parse_row(rows[2])
    return {
        'freq': freq_data,
        'vout_mag': vout_mag_data,
        'vout_phase': vout_phase_data,
    }

def create_freq_response_plot():

    RESISTANCE_OHMS = 1e3
    CAPACITANCE_FARADS = 1e-6
    V_IN_VOLTS = 5.0

    LOG_X_MIN = 0
    LOG_X_MAX = 5

    freq_data = np.logspace(LOG_X_MIN, LOG_X_MAX, num=100)

    # Xc = 1 / (2pi fC)
    x_c_data = 1 / (2*np.pi*freq_data*CAPACITANCE_FARADS)

    # Vout = Vin * (Xc / ( sqrt(Xc^2 + R^2) ))
    v_out_data = V_IN_VOLTS*(x_c_data/np.sqrt(x_c_data**2 + RESISTANCE_OHMS**2))

    phase_shift_deg = np.rad2deg(-1*np.arctan(2*np.pi*freq_data*RESISTANCE_OHMS*CAPACITANCE_FARADS))

    fig, ax = plt.subplots(1)

    line1, = ax.plot(freq_data, v_out_data, label='$|V_{out}|$')
    ax2 = ax.twinx()
    line2, = ax2.plot(freq_data, phase_shift_deg, label='$\phi(V_{out})$', color='C2')

    f_cutoff = 1 / (2*np.pi*RESISTANCE_OHMS*CAPACITANCE_FARADS)
    ax.axvline(x=f_cutoff, color='C1')

    ax.set_xscale('log')
    ax.set_xlabel('Frequency f (Hz)')

    x_ticks = [ 10**x for x in range(LOG_X_MIN, LOG_X_MAX + 1) ]
    x_ticks_labels = [ str(x) for x in x_ticks ]
    x_ticks.append(f_cutoff)
    x_ticks_labels.append('$f_c$')

    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_ticks_labels)
    ax.set
    ax.set_ylabel('$V_{out}$ Magnitude V (V)')

    ax2.set_ylabel('$V_{out}$ Phase $\phi$ (deg)')
    ax2.set_ylim(-135, 45)

    ax.set_title('Frequency Response of a Low-Pass RC Filter')

    lines = [ line1, line2 ]
    ax.legend(lines, [line.get_label() for line in lines ])

    plt.tight_layout()
    plt.savefig('rc-low-pass-filter-frequency-response.png')

def create_sallen_key_response_plot(data_dir):
        # Low-pass filter comparison plots

    sim_results_path = data_dir / 'sim-results.csv'

    data = get_freq_mag_phase(sim_results_path)

    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(8, 5), squeeze=False)

    ax = axes[0][0]
    color = 'C0'
    ln1 = ax.plot(data['freq'], data['vout_mag'], label='Gain', color=color)
    ax.set_xlabel('Frequency f (Hz)')
    ax.set_xscale('log')
    ax.set_ylabel('Gain (dB)', color=color)
    ax.tick_params(axis='y', labelcolor=color)

    ax2 = ax.twinx()
    color = 'C1'
    ln2 = ax2.plot(data['freq'], data['vout_phase'], label='Phase', color=color)
    ax2.set_ylabel('Phase Shift ($^{\circ}$)', color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    lns = ln1 + ln2
    labs = [l.get_label() for l in lns]
    ax.legend(lns, labs, loc=0)
    ax.axvline(1e3, color='gray', linestyle='--') # Add line at fc

    ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=15))
    # ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
    ax.grid(which='major', alpha=1.0, linestyle='-')
    ax.grid(which='minor', alpha=0.6, linestyle='--')

    plt.tight_layout()
    plot_path = data_dir / 'response.png'
    plt.savefig(plot_path)


def create_low_pass_filter_comparison_plots(config):
    # Low-pass filter comparison plots

    data = [ get_freq_mag_phase(config_entry['data_path']) for config_entry in config ]
    xlim = [1e1, 1e4]

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

    ax = axes[0]
    for idx, config_entry in enumerate(config):
        db_gain = data[idx]['vout_mag']
        ax.plot(data[idx]['freq'], db_gain, label=config_entry['legend'])
    ax.set_title('Gain Response Of Different Low-Pass Filter Optimizations/Tunings\nfc=1kHz')
    ax.set_xlabel('Frequency f (Hz)')
    ax.set_xscale('log')
    ax.set_xlim(xlim)
    ax.set_ylabel('Gain (dB)')
    ax.axvline(1e3, color='gray', linestyle='--') # Add line at fc
    ax.legend()
    ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=15))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
    ax.grid(which='major', alpha=1.0, linestyle='-')
    ax.grid(which='minor', alpha=0.6, linestyle='--')

    ax = axes[1]
    for idx, config_entry in enumerate(config):
        ax.plot(data[idx]['freq'], data[idx]['vout_phase'], label=config_entry['legend'])
    ax.set_title('Phase Response Of Different Low-Pass Filter Optimizations/Tunings\nfc=1kHz')
    ax.set_xlabel('Frequency f (Hz)')
    ax.set_xscale('log')
    ax.set_xlim(xlim)
    ax.set_ylabel('Phase Shift ($^\circ$)')
    ax.axvline(1e3, color='gray', linestyle='--') # Add line at fc
    ax.legend()
    ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(90)) # 90 makes sense for phase angle
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(45)) # 45 makes sense for phase angle
    ax.grid(which='major', alpha=1.0, linestyle='-')
    ax.grid(which='minor', alpha=0.6, linestyle='--')

    plt.tight_layout()
    plot_path = 'low-pass-filter-optimization-comparison-gain-db.png'
    plt.savefig(plot_path)


    # Separate file for V/V gain
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

    ax = axes[0]
    for idx, config_entry in enumerate(config):
        db_gain = data[idx]['vout_mag']
        voltage_gain = np.power(10, db_gain/20)
        ax.plot(data[idx]['freq'], voltage_gain, label=config_entry['legend'])
    ax.set_title('Gain Response Of Different Low-Pass Filter Optimizations/Tunings\nfc=1kHz')
    ax.set_xlabel('Frequency f (Hz)')
    ax.set_xscale('log')
    ax.set_xlim(xlim)
    ax.set_ylabel('Gain (V/V)')
    ax.axvline(1e3, color='gray', linestyle='--') # Add line at fc
    ax.legend()
    ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
    ax.grid(which='major', alpha=1.0, linestyle='-')
    ax.grid(which='minor', alpha=0.6, linestyle='--')


    ax = axes[1]
    for idx, config_entry in enumerate(config):
        ax.plot(data[idx]['freq'], data[idx]['vout_phase'], label=config_entry['legend'])
    ax.set_title('Phase Response Of Different Low-Pass Filter Optimizations/Tunings\nfc=1kHz')
    ax.set_xlabel('Frequency f (Hz)')
    ax.set_xscale('log')
    ax.set_xlim(xlim)
    ax.set_ylabel('Phase Shift ($^\circ$)')
    ax.axvline(1e3, color='gray', linestyle='--') # Add line at fc
    ax.legend()
    ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(90)) # 90 makes sense for phase angle
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(45)) # 45 makes sense for phase angle
    ax.grid(which='major', alpha=1.0, linestyle='-')
    ax.grid(which='minor', alpha=0.6, linestyle='--')

    plt.tight_layout()
    plot_path = 'low-pass-filter-optimization-comparison-gain-vv.png'
    plt.savefig(plot_path)

    # Plot of phase difference with linear x-axis, helps visualize the linear
    # response of the Bessel filter
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(7, 7), squeeze=False)

    ax = axes[0][0]
    for idx, config_entry in enumerate(config):
        ax.plot(data[idx]['freq'], data[idx]['vout_phase'], label=config_entry['legend'])
    ax.set_xlabel('Frequency f (Hz)')
    # ax.set_xscale('log')
    ax.set_xlim([0, 2e3])
    ax.set_ylabel('Phase Shift ($^\circ$)')
    ax.axvline(1e3, color='gray', linestyle='--') # Add line at fc
    ax.legend()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1000))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(100))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(90)) # 90 makes sense for phase angle
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(45)) # 45 makes sense for phase angle
    ax.grid(which='major', alpha=1.0, linestyle='-')
    ax.grid(which='minor', alpha=0.6, linestyle='--')

    plt.tight_layout()
    plot_path = 'low-pass-filter-optimization-comparison-phase-linear.png'
    plt.savefig(plot_path)

def create_sallen_key_bode_plot_showing_gain_rise():

    data_dir_path = Path('low-pass-sallen-key-showing-gain-rise')

    # Get data
    data = get_freq_mag_phase(data_dir_path / 'sim-results.csv')

    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(7, 7), squeeze=False)

    ax = axes[0][0]
    ax.plot(data['freq'], data['vout_mag'], label='Sallen-Key Low-Pass')
    ax.set_xlabel('Frequency f (Hz)')
    ax.set_xscale('log')
    # ax.set_xlim(xlim)
    ax.set_ylabel('Gain (dB)')
    ax.axvline(1e3, color='gray', linestyle='--') # Add line at fc
    ax.legend()

    # ax.grid(b=True, which='major', color='#666666', linestyle='-')
    # Show the minor grid lines with very faint and almost transparent grey lines
    # ax.minorticks_on()
    # ax.xaxis.set_minor_locator(MultipleLocator(1000000))
    # ax.yaxis.set_minor_locator(MultipleLocator(10))
    # ax.xaxis.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    # ax.grid(True, which='both')
    ax.xaxis.set_minor_locator(ticker.LogLocator(base=10.0, numticks=15))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
    ax.grid(which='major', alpha=1.0, linestyle='-')
    ax.grid(which='minor', alpha=0.6, linestyle='--')

    plt.tight_layout()
    plt.savefig(data_dir_path / 'response.png')

from sympy import *
import math
from tabulate import tabulate
from bs4 import BeautifulSoup
def create_butterworth_table():
    
    def create_polynomial_expr(n):
        """
        Generates a printable sympy expression of the factored Butterworth polynomial of degree n  
        Polynomial equations from https://tttapa.github.io/Pages/Mathematics/Systems-and-Control-Theory/Analog-Filters/Butterworth-Filters.html
        """
        init_printing(use_unicode=True)
        s = symbols('s')        
        if n % 2 == 0:
            # n is even
            end = n//2
            output = 1
        else:
            # n is off
            output = (s + 1)
            end = (n - 1)//2
        # The rest is the same regardless of odd or even
        for k in range(end):
            # The round to 3 decimal places below keeps the printed number sensible
            output *= (s**2 - round(2*math.cos(2*math.pi*(2*k + n + 1)/(4*n)), 3)*s + 1)
        return output

    table = [['n', 'poly']]
    for i in range(1, 9):
        poly = create_polynomial_expr(i)
        # If we are a 1st or 2nd order filter, add brackets manually as these
        # are removed by sympy
        if i == 1 or i == 2:
            table.append([f'{i}', f'\(({latex(poly)})\)'])
        else:
            table.append([f'{i}', f'\({latex(poly)}\)'])

    html_table = tabulate(table, headers='firstrow', tablefmt='html')
    soup = BeautifulSoup(html_table, features='html.parser')
    
    # Add a fixed width to column with latex equations in it, otherwise the table width goes crazy
    second_col = soup.table.thead.tr.find_all('th')[1]
    second_col['style'] = 'width: 700px;'
    print(soup.prettify())


if __name__ == '__main__':
    main()
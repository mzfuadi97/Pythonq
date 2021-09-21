{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Data Quality.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "S-vzFjN8LOBV"
      },
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import io\n",
        "import pandas_profiling\n",
        "retail_raw = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced_data_quality.csv')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "k7o-r3_QLrEx",
        "outputId": "97dd8be7-ce48-4bd2-e9ca-ff25b6bef4fd"
      },
      "source": [
        "# Cetak tipe data di setiap kolom retail_raw\n",
        "print(retail_raw.dtypes)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "order_id         int64\n",
            "order_date      object\n",
            "customer_id      int64\n",
            "city            object\n",
            "province        object\n",
            "product_id      object\n",
            "brand           object\n",
            "quantity       float64\n",
            "item_price     float64\n",
            "dtype: object\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0h-9gir7LxaH",
        "outputId": "5fe86a14-2036-4014-c1e3-ac3866071433"
      },
      "source": [
        "# Kolom city\n",
        "length_city = len(retail_raw['city'])\n",
        "print('Length kolom city:', length_city)\n",
        "\n",
        "# Tugas Praktek: Kolom product_id\n",
        "length_product_id = len(retail_raw['product_id'])\n",
        "print('Length kolom product_id:', length_product_id)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Length kolom city: 5000\n",
            "Length kolom product_id: 5000\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0FjGVTo3Lz_z",
        "outputId": "fff7b38e-d14e-40d1-ade1-ece785db82f4"
      },
      "source": [
        "# Count kolom city\n",
        "count_city = retail_raw['city'].count()\n",
        "print('Count kolom count_city:', count_city)\n",
        "\n",
        "# Tugas praktek: count kolom product_id\n",
        "count_product_id = retail_raw['product_id'].count()\n",
        "print('Count kolom product_id:', count_product_id)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Count kolom count_city: 4984\n",
            "Count kolom product_id: 4989\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZFRt0pjdMbB8",
        "outputId": "28fadd6a-4737-4c73-ce1d-b6d6906f7ae3"
      },
      "source": [
        "# Missing value pada kolom city\n",
        "number_of_missing_values_city = length_city - count_city\n",
        "float_of_missing_values_city = float(number_of_missing_values_city/length_city)\n",
        "pct_of_missing_values_city = '{0:.1f}%'.format(float_of_missing_values_city * 100)\n",
        "print('Persentase missing value kolom city:', pct_of_missing_values_city)\n",
        "\n",
        "# Tugas praktek: Missing value pada kolom product_id\n",
        "number_of_missing_values_product_id = length_product_id - count_product_id\n",
        "float_of_missing_values_product_id = float(number_of_missing_values_product_id/length_product_id)\n",
        "pct_of_missing_values_product_id = '{0:.1f}%'.format(float_of_missing_values_product_id * 100)\n",
        "print('Persentase missing value kolom product_id:', pct_of_missing_values_product_id)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Persentase missing value kolom city: 0.3%\n",
            "Persentase missing value kolom product_id: 0.2%\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zIsTN4NdMnY0",
        "outputId": "854edb23-c2d0-4666-b3a9-882b74b59ebf"
      },
      "source": [
        "\n",
        "# Deskriptif statistics kolom quantity\n",
        "print('Kolom quantity')\n",
        "print('Minimum value: ', retail_raw['quantity'].min())\n",
        "print('Maximum value: ', retail_raw['quantity'].max())\n",
        "print('Mean value: ', retail_raw['quantity'].mean())\n",
        "print('Mode value: ', retail_raw['quantity'].mode())\n",
        "print('Median value: ', retail_raw['quantity'].median())\n",
        "print('Standard Deviation value: ', retail_raw['quantity'].std())\n",
        "\n",
        "# Tugas praktek: Deskriptif statistics kolom item_price\n",
        "print('')\n",
        "print('Kolom item_price')\n",
        "print('Minimum value: ', retail_raw['item_price'].min())\n",
        "print('Maximum value: ', retail_raw['item_price'].max())\n",
        "print('Mean value: ', retail_raw['item_price'].mean())\n",
        "print('Median value: ', retail_raw['item_price'].median())\n",
        "print('Standard Deviation value: ', retail_raw['item_price'].std())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Kolom quantity\n",
            "Minimum value:  1.0\n",
            "Maximum value:  720.0\n",
            "Mean value:  11.423987164059366\n",
            "Mode value:  0    1.0\n",
            "dtype: float64\n",
            "Median value:  5.0\n",
            "Standard Deviation value:  29.442025010811317\n",
            "\n",
            "Kolom item_price\n",
            "Minimum value:  26000.0\n",
            "Maximum value:  29762000.0\n",
            "Mean value:  933742.7311008623\n",
            "Median value:  604000.0\n",
            "Standard Deviation value:  1030829.8104242863\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0EjhU3kOM367",
        "outputId": "a90468bc-4f37-4393-e28d-bb12fc8c3960"
      },
      "source": [
        "# Quantile statistics kolom quantity\n",
        "print('Kolom quantity:')\n",
        "print(retail_raw['quantity'].quantile([0.25, 0.5, 0.75]))\n",
        "\n",
        "# Tugas praktek: Quantile statistics kolom item_price\n",
        "print('')\n",
        "print('Kolom item_price:')\n",
        "print(retail_raw['item_price'].quantile([0.25, 0.5, 0.75]))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Kolom quantity:\n",
            "0.25     2.0\n",
            "0.50     5.0\n",
            "0.75    12.0\n",
            "Name: quantity, dtype: float64\n",
            "\n",
            "Kolom item_price:\n",
            "0.25     450000.0\n",
            "0.50     604000.0\n",
            "0.75    1045000.0\n",
            "Name: item_price, dtype: float64\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DWQiHgSSNuHj",
        "outputId": "89ea792a-9246-41b3-b601-10670e3b3d51"
      },
      "source": [
        "print('Korelasi quantity dengan item_price')\n",
        "print(retail_raw[['quantity', 'item_price']].corr())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Korelasi quantity dengan item_price\n",
            "            quantity  item_price\n",
            "quantity    1.000000   -0.133936\n",
            "item_price -0.133936    1.000000\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iNJGl4dzOYSK"
      },
      "source": [
        "## Data Cleansing"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8Ao2NxS0OCpI",
        "outputId": "8d0fa995-3d77-48ea-9124-b1d38bd2a937"
      },
      "source": [
        "# Check kolom yang memiliki missing data\n",
        "print('Check kolom yang memiliki missing data:')\n",
        "print(retail_raw.isnull().any())\n",
        "\n",
        "# Filling the missing value (imputasi)\n",
        "print('\\nFilling the missing value (imputasi):')\n",
        "print(retail_raw['quantity'].fillna(retail_raw.quantity.mean()))\n",
        "\n",
        "# Drop missing value\n",
        "print('\\nDrop missing value:')\n",
        "print(retail_raw['quantity'].dropna())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Check kolom yang memiliki missing data:\n",
            "order_id       False\n",
            "order_date     False\n",
            "customer_id    False\n",
            "city            True\n",
            "province        True\n",
            "product_id      True\n",
            "brand          False\n",
            "quantity        True\n",
            "item_price      True\n",
            "dtype: bool\n",
            "\n",
            "Filling the missing value (imputasi):\n",
            "0       10.0\n",
            "1        2.0\n",
            "2        8.0\n",
            "3        4.0\n",
            "4        2.0\n",
            "        ... \n",
            "4995     2.0\n",
            "4996     3.0\n",
            "4997     4.0\n",
            "4998     8.0\n",
            "4999     1.0\n",
            "Name: quantity, Length: 5000, dtype: float64\n",
            "\n",
            "Drop missing value:\n",
            "0       10.0\n",
            "1        2.0\n",
            "2        8.0\n",
            "3        4.0\n",
            "4        2.0\n",
            "        ... \n",
            "4995     2.0\n",
            "4996     3.0\n",
            "4997     4.0\n",
            "4998     8.0\n",
            "4999     1.0\n",
            "Name: quantity, Length: 4986, dtype: float64\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XwOItIRtOajH",
        "outputId": "f8171fab-e58a-47cb-f237-655e6f59d746"
      },
      "source": [
        "print(retail_raw['item_price'].fillna(retail_raw['item_price'].mean()))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "0       7.400000e+05\n",
            "1       6.040000e+05\n",
            "2       1.045000e+06\n",
            "3       2.050000e+05\n",
            "4       9.337427e+05\n",
            "            ...     \n",
            "4995    4.500000e+05\n",
            "4996    1.465000e+06\n",
            "4997    7.470000e+05\n",
            "4998    6.950000e+05\n",
            "4999    1.045000e+06\n",
            "Name: item_price, Length: 5000, dtype: float64\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qwBzjJcvOtQ5",
        "outputId": "5bc92415-e668-4b3c-a8d1-cc7d7c1afae2"
      },
      "source": [
        "# Q1, Q3, dan IQR\n",
        "Q1 = retail_raw['quantity'].quantile(0.25)\n",
        "Q3 = retail_raw['quantity'].quantile(0.75)\n",
        "IQR = Q3 - Q1\n",
        "\n",
        "# Check ukuran (baris dan kolom) sebelum data yang outliers dibuang\n",
        "print('Shape awal: ', retail_raw.shape)\n",
        "\n",
        "# Removing outliers\n",
        "retail_raw = retail_raw[~((retail_raw['quantity'] < (Q1 - 1.5 * IQR)) | (retail_raw['quantity'] > (Q3 + 1.5 * IQR)))]\n",
        "\n",
        "# Check ukuran (baris dan kolom) setelah data yang outliers dibuang\n",
        "print('Shape akhir: ', retail_raw.shape)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Shape awal:  (5000, 9)\n",
            "Shape akhir:  (4699, 9)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eiFaiycEO6R3",
        "outputId": "f02408a2-3e9a-4691-fdee-c153138ff7e2"
      },
      "source": [
        "# Q1, Q3, dan IQR\n",
        "Q1 = retail_raw['item_price'].quantile(0.25)\n",
        "Q3 = retail_raw['item_price'].quantile(0.75)\n",
        "IQR = Q3 - Q1\n",
        "\n",
        "# Check ukuran (baris dan kolom) sebelum data yang outliers dibuang\n",
        "print('Shape awal: ', retail_raw.shape)\n",
        "\n",
        "# Removing outliers\n",
        "retail_raw = retail_raw[~((retail_raw['item_price'] < (Q1 - 1.5 * IQR)) | (retail_raw['item_price'] > (Q3 + 1.5 * IQR)))]\n",
        "\n",
        "# Check ukuran (baris dan kolom) setelah data yang outliers dibuang\n",
        "print('Shape akhir: ', retail_raw.shape)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Shape awal:  (4699, 9)\n",
            "Shape akhir:  (4379, 9)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "L2H4CXhuPJDI"
      },
      "source": [
        "## Dedupliklasi\n",
        "\n",
        "Duplikasi data merupakan data dengan kondisi pada row-row tertentu memiliki kesamaan data di seluruh kolomnya. Tentunya ada data yang duplikat dalam dataset yang dimiliki. Kondisi duplikasi harus diatasi dengan jalan mengeliminir baris yang mengalami duplikasi, sehingga proses ini dikenal dengan deduplikasi."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c8IfYaa9PBzo",
        "outputId": "280819e4-8cbc-42dd-a7ef-8c4320e54f77"
      },
      "source": [
        "# Check ukuran (baris dan kolom) sebelum data duplikasi dibuang\n",
        "print('Shape awal: ', retail_raw.shape)\n",
        "\n",
        "# Buang data yang terduplikasi\n",
        "retail_raw.drop_duplicates(inplace=True)\n",
        "\n",
        "# Check ukuran (baris dan kolom) setelah data duplikasi dibuang\n",
        "print('Shape akhir: ', retail_raw.shape)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Shape awal:  (4379, 9)\n",
            "Shape akhir:  (4373, 9)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EBNzA5OWPrYa"
      },
      "source": [
        "## Data Profiling\n",
        "\n",
        "Inspeksi dataframe uncleaned_raw\n",
        "Check kolom yang mengandung missing value, jika ada, kolom apakah itu dan berapa persen missing value pada kolom tersebut?\n",
        "Mengisi missing value tersebut dengan mean dari kolom tersebut!"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kb0NFMqKPUil",
        "outputId": "396db4e2-ad49-4bf6-8544-afb78bf38dfb"
      },
      "source": [
        "# Baca dataset uncleaned_raw.csv\n",
        "uncleaned_raw = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/uncleaned_raw.csv')\n",
        "\n",
        "#inspeksi dataframe uncleaned_raw\n",
        "print('Lima data teratas:') \n",
        "print(uncleaned_raw.head())\n",
        "\n",
        "#Check kolom yang mengandung missing value\n",
        "print('\\nKolom dengan missing value:') \n",
        "print(uncleaned_raw.isnull().any())\n",
        "\n",
        "#Persentase missing value\n",
        "length_qty = len(uncleaned_raw['Quantity'])\n",
        "count_qty = uncleaned_raw['Quantity'].count()\n",
        "\n",
        "#mengurangi length dengan count\n",
        "number_of_missing_values_qty = length_qty - count_qty\n",
        "\n",
        "#mengubah ke bentuk float\n",
        "float_of_missing_values_qty = float(number_of_missing_values_qty / length_qty) \n",
        "\n",
        "#mengubah ke dalam bentuk persen\n",
        "pct_of_missing_values_qty = '{0:.1f}%'.format(float_of_missing_values_qty*100) \n",
        "\n",
        "#print hasil percent dari missing value\n",
        "print('Persentase missing value kolom Quantity:', pct_of_missing_values_qty)\n",
        "\n",
        "#Mengisi missing value tersebut dengan mean dari kolom tersebut\n",
        "uncleaned_raw['Quantity'] = uncleaned_raw['Quantity'].fillna(uncleaned_raw['Quantity'].mean())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Lima data teratas:\n",
            "   InvoiceNo                          Description  ...  CustomerID      City\n",
            "0     536365   WHITE HANGING HEART T-LIGHT HOLDER  ...       17850  Surabaya\n",
            "1     536366                  WHITE METAL LANTERN  ...       17850  Surabaya\n",
            "2     536367       CREAM CUPID HEARTS COAT HANGER  ...       17850  Surabaya\n",
            "3     536368  KNITTED UNION FLAG HOT WATER BOTTLE  ...       17850   Jakarta\n",
            "4     536369       RED WOOLLY HOTTIE WHITE HEART.  ...       17850     Medan\n",
            "\n",
            "[5 rows x 7 columns]\n",
            "\n",
            "Kolom dengan missing value:\n",
            "InvoiceNo      False\n",
            "Description    False\n",
            "Quantity        True\n",
            "InvoiceDate    False\n",
            "UnitPrice      False\n",
            "CustomerID     False\n",
            "City           False\n",
            "dtype: bool\n",
            "Persentase missing value kolom Quantity: 4.0%\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wXQm4NsRP5xh"
      },
      "source": [
        "## Data Cleansing\n",
        "\n",
        "Mengetahui kolom yang memiliki outliers! Gunakan visualisasi dengan boxplot pada dataframe uncleaned_raw."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 276
        },
        "id": "HEFLSiNUPzaN",
        "outputId": "fa0ad349-0747-439e-ffb8-9b17059c6e46"
      },
      "source": [
        "import matplotlib.pyplot as plt\n",
        "\n",
        "#Mengetahui kolom yang memiliki outliers!\n",
        "uncleaned_raw.boxplot()\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eABCf0D8QMu6"
      },
      "source": [
        "Melakukan proses removing outliers pada kolom UnitPrice.\n",
        "Checking duplikasi and melakukan deduplikasi dataset tersebut"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BaYovsb-P8Cu",
        "outputId": "1073b5df-f67e-4345-9ce9-6690beac165b"
      },
      "source": [
        "#Check IQR\n",
        "Q1 = uncleaned_raw['UnitPrice'].quantile(0.25)\n",
        "Q3 = uncleaned_raw['UnitPrice'].quantile(0.75)\n",
        "IQR = Q3 - Q1\n",
        "\n",
        "#removing outliers\n",
        "uncleaned_raw = uncleaned_raw[~((uncleaned_raw[['UnitPrice']] < (Q1 - 1.5 * IQR)) | (uncleaned_raw[['UnitPrice']] > (Q3 + 1.5 * IQR)))]\n",
        "\n",
        "#check for duplication\n",
        "print(uncleaned_raw.duplicated(subset=None))\n",
        "\n",
        "#remove duplication\n",
        "uncleaned_raw = uncleaned_raw.drop_duplicates()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "0      False\n",
            "1      False\n",
            "2      False\n",
            "3      False\n",
            "4      False\n",
            "       ...  \n",
            "500     True\n",
            "501     True\n",
            "502     True\n",
            "503     True\n",
            "504     True\n",
            "Length: 505, dtype: bool\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "t65F62H7QLB_"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
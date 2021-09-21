{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Building Recommended System.ipynb",
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
        "id": "9Cd4ZAhusSQj"
      },
      "source": [
        "#import library yang dibutuhkan\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "\n",
        "#lakukan pembacaan dataset\n",
        "movie_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/title.basics.tsv', sep='\\t') #untuk menyimpan title_basics.tsv\n",
        "rating_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/title.ratings.tsv', sep='\\t') #untuk menyimpan title.ratings.tsv"
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
        "id": "Pt30XV1GuGiD",
        "outputId": "eb2a888b-6008-45aa-bf82-6c1afb60d1d7"
      },
      "source": [
        "print(movie_df.info())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 9025 entries, 0 to 9024\n",
            "Data columns (total 9 columns):\n",
            " #   Column          Non-Null Count  Dtype \n",
            "---  ------          --------------  ----- \n",
            " 0   tconst          9025 non-null   object\n",
            " 1   titleType       9025 non-null   object\n",
            " 2   primaryTitle    9011 non-null   object\n",
            " 3   originalTitle   9011 non-null   object\n",
            " 4   isAdult         9025 non-null   int64 \n",
            " 5   startYear       9025 non-null   object\n",
            " 6   endYear         9025 non-null   object\n",
            " 7   runtimeMinutes  9025 non-null   object\n",
            " 8   genres          9014 non-null   object\n",
            "dtypes: int64(1), object(8)\n",
            "memory usage: 634.7+ KB\n",
            "None\n"
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
        "id": "cgJNske4sWLo",
        "outputId": "1e083532-0552-4ca2-b629-995e63705ba5"
      },
      "source": [
        "print(movie_df.isna().sum())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "tconst             0\n",
            "titleType          0\n",
            "primaryTitle      14\n",
            "originalTitle     14\n",
            "isAdult            0\n",
            "startYear          0\n",
            "endYear            0\n",
            "runtimeMinutes     0\n",
            "genres            11\n",
            "dtype: int64\n"
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
        "id": "mBBbXnXGuR-i",
        "outputId": "7fb553ce-429e-4390-ff64-8ea02de78204"
      },
      "source": [
        "print(movie_df.loc[(movie_df['primaryTitle'].isnull()) | (movie_df['originalTitle'].isnull())])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "          tconst  titleType  ... runtimeMinutes                genres\n",
            "9000  tt10790040  tvEpisode  ...             \\N                    \\N\n",
            "9001  tt10891902  tvEpisode  ...             \\N                 Crime\n",
            "9002  tt11737860  tvEpisode  ...             \\N  Comedy,Drama,Romance\n",
            "9003  tt11737862  tvEpisode  ...             \\N  Comedy,Drama,Romance\n",
            "9004  tt11737866  tvEpisode  ...             \\N  Comedy,Drama,Romance\n",
            "9005  tt11737872  tvEpisode  ...             \\N                    \\N\n",
            "9006  tt11737874  tvEpisode  ...             \\N  Comedy,Drama,Romance\n",
            "9007   tt1971246  tvEpisode  ...             \\N             Biography\n",
            "9008   tt2067043  tvEpisode  ...             \\N                 Music\n",
            "9009   tt4404732  tvEpisode  ...             \\N                Comedy\n",
            "9010   tt5773048  tvEpisode  ...             \\N             Talk-Show\n",
            "9011   tt8473688  tvEpisode  ...             \\N                 Drama\n",
            "9012   tt8541336  tvEpisode  ...             \\N    Reality-TV,Romance\n",
            "9013   tt9824302  tvEpisode  ...             \\N           Documentary\n",
            "\n",
            "[14 rows x 9 columns]\n"
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
        "id": "ArJgYYmhx2bV",
        "outputId": "abba3de9-113d-4c91-953d-71d2f0927b44"
      },
      "source": [
        "#mengupdate movie_df dengan membuang data-data bernilai NULL\n",
        "movie_df = movie_df.loc[(movie_df['primaryTitle'].notnull()) & (movie_df['originalTitle'].notnull())]\n",
        "\n",
        "#Menampilkan jumlah data setelah data dengan nilai NULL dibuang\n",
        "print(len(movie_df))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "9011\n"
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
        "id": "Dx6QHmeszVQs",
        "outputId": "7b6451ca-b3c2-4af5-89be-5d4cbd908e57"
      },
      "source": [
        "print(movie_df.loc[movie_df['genres'].isnull()])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "          tconst  titleType  ...          runtimeMinutes genres\n",
            "9014  tt10233364  tvEpisode  ...              Reality-TV    NaN\n",
            "9015  tt10925142  tvEpisode  ...               Talk-Show    NaN\n",
            "9016  tt10970874  tvEpisode  ...                      \\N    NaN\n",
            "9017  tt11670006  tvEpisode  ...             Documentary    NaN\n",
            "9018  tt11868642  tvEpisode  ...               Talk-Show    NaN\n",
            "9019   tt2347742  tvEpisode  ...                      \\N    NaN\n",
            "9020   tt3984412  tvEpisode  ...              Reality-TV    NaN\n",
            "9021   tt8740950  tvEpisode  ...              Reality-TV    NaN\n",
            "9022   tt9822816  tvEpisode  ...                      \\N    NaN\n",
            "9023   tt9900062  tvEpisode  ...  Animation,Comedy,Drama    NaN\n",
            "9024   tt9909210  tvEpisode  ...                      \\N    NaN\n",
            "\n",
            "[11 rows x 9 columns]\n"
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
        "id": "ku1nwik-zzt1",
        "outputId": "e8c9e1f5-9c54-48e8-c91c-8838dc5896a6"
      },
      "source": [
        "#mengupdate movie_df dengan membuang data-data bernilai NULL\n",
        "movie_df = movie_df.loc[movie_df['genres'].notnull()]\n",
        "\n",
        "#Menampilkan jumlah data setelah data dengan nilai NULL dibuang\n",
        "print(len(movie_df))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "9000\n"
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
        "id": "ziRjvHvHz-04",
        "outputId": "7fbaea13-2df4-4ee0-dd51-e5f7e9a04801"
      },
      "source": [
        "#mengubah nilai '\\\\N' pada startYear menjadi np.nan dan cast kolomnya menjadi float64\n",
        "movie_df['startYear'] = movie_df['startYear'].replace('\\\\N', np.nan)\n",
        "movie_df['startYear'] = movie_df['startYear'].astype('float64')\n",
        "print(movie_df['startYear'].unique()[:5])\n",
        "\n",
        "#mengubah nilai '\\\\N' pada endYear menjadi np.nan dan cast kolomnya menjadi float64\n",
        "movie_df['endYear'] = movie_df['endYear'].replace('\\\\N', np.nan)\n",
        "movie_df['endYear'] = movie_df['endYear'].astype('float64')\n",
        "print(movie_df['endYear'].unique()[:5])\n",
        "\n",
        "#mengubah nilai '\\\\N' pada runtimeMinutes menjadi np.nan dan cast kolomnya menjadi float64\n",
        "movie_df['runtimeMinutes'] = movie_df['runtimeMinutes'].replace('\\\\N', np.nan)\n",
        "movie_df['runtimeMinutes'] = movie_df['runtimeMinutes'].astype('float64')\n",
        "print(movie_df['runtimeMinutes'].unique()[:5])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1898. 2018. 2016. 1987. 1973.]\n",
            "[  nan 2005. 1955. 2006. 1999.]\n",
            "[nan 29.  7. 23. 85.]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bkS6yY4u0XJ3"
      },
      "source": [
        "#Membuat fungsi transform_to_list\n",
        "def transform_to_list(x):\n",
        "    if ',' in x: \n",
        "    #ubah menjadi list apabila ada data pada kolom genre\n",
        "        return x.split(',')\n",
        "    else: \n",
        "    #jika tidak ada data, ubah menjadi list kosong\n",
        "        return []\n",
        "\n",
        "movie_df['genres'] = movie_df['genres'].apply(lambda x: transform_to_list(x))\n"
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
        "id": "1y5_nUb52Oel",
        "outputId": "43e5c65a-5e55-4858-d91d-87012acea890"
      },
      "source": [
        "#Menampilkan 5 data teratas rating_df\n",
        "print(\"5 data teratas\")\n",
        "print(rating_df.head())\n",
        "#Melihat tipe data setiap kolom\n",
        "print(\"Tipe Data setiap Kolom\")\n",
        "print(rating_df.info())\n",
        "#Pengecekan Data dengan Nilai NULL\n",
        "print(\"Data dengan Nilai NULL\")\n",
        "print(rating_df.isnull().sum())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "5 data teratas\n",
            "      tconst  averageRating  numVotes\n",
            "0  tt0000001            5.6      1608\n",
            "1  tt0000002            6.0       197\n",
            "2  tt0000003            6.5      1285\n",
            "3  tt0000004            6.1       121\n",
            "4  tt0000005            6.1      2050\n",
            "Tipe Data setiap Kolom\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 1030009 entries, 0 to 1030008\n",
            "Data columns (total 3 columns):\n",
            " #   Column         Non-Null Count    Dtype  \n",
            "---  ------         --------------    -----  \n",
            " 0   tconst         1030009 non-null  object \n",
            " 1   averageRating  1030009 non-null  float64\n",
            " 2   numVotes       1030009 non-null  int64  \n",
            "dtypes: float64(1), int64(1), object(1)\n",
            "memory usage: 23.6+ MB\n",
            "None\n",
            "Data dengan Nilai NULL\n",
            "tconst           0\n",
            "averageRating    0\n",
            "numVotes         0\n",
            "dtype: int64\n"
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
        "id": "De1ZZqb02p_O",
        "outputId": "d7dfe9a2-7f3c-4254-88db-cbe8bdc66c3f"
      },
      "source": [
        "#Lakukan join pada kedua table\n",
        "movie_rating_df = pd.merge(movie_df, rating_df, on='tconst', how='inner')\n",
        "\n",
        "#Tampilkan 5 data teratas\n",
        "print(movie_rating_df.head())\n",
        "\n",
        "#Tampilkan tipe data dari tiap kolom\n",
        "print(movie_rating_df.info())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "      tconst  titleType  ... averageRating numVotes\n",
            "0  tt0043745      short  ...           7.1      459\n",
            "1  tt0167491      video  ...           5.7        7\n",
            "2  tt6574096  tvEpisode  ...           8.5      240\n",
            "3  tt6941700  tvEpisode  ...           8.0       11\n",
            "4  tt7305674      video  ...           9.7        7\n",
            "\n",
            "[5 rows x 11 columns]\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Int64Index: 1376 entries, 0 to 1375\n",
            "Data columns (total 11 columns):\n",
            " #   Column          Non-Null Count  Dtype  \n",
            "---  ------          --------------  -----  \n",
            " 0   tconst          1376 non-null   object \n",
            " 1   titleType       1376 non-null   object \n",
            " 2   primaryTitle    1376 non-null   object \n",
            " 3   originalTitle   1376 non-null   object \n",
            " 4   isAdult         1376 non-null   int64  \n",
            " 5   startYear       1376 non-null   float64\n",
            " 6   endYear         26 non-null     float64\n",
            " 7   runtimeMinutes  1004 non-null   float64\n",
            " 8   genres          1376 non-null   object \n",
            " 9   averageRating   1376 non-null   float64\n",
            " 10  numVotes        1376 non-null   int64  \n",
            "dtypes: float64(4), int64(2), object(5)\n",
            "memory usage: 129.0+ KB\n",
            "None\n"
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
        "id": "QeKXmacG4LQM",
        "outputId": "14d09076-4504-4e32-d394-25f89ea499be"
      },
      "source": [
        "#Menghilangkan semua nilai NULL dari kolom startYear dan runtimeMinutes\n",
        "movie_rating_df = movie_rating_df.dropna(subset=['startYear','runtimeMinutes'])\n",
        "\n",
        "#Untuk memastikan bahwa sudah tidak ada lagi nilai NULL\n",
        "print(movie_rating_df.info())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Int64Index: 1004 entries, 0 to 1374\n",
            "Data columns (total 11 columns):\n",
            " #   Column          Non-Null Count  Dtype  \n",
            "---  ------          --------------  -----  \n",
            " 0   tconst          1004 non-null   object \n",
            " 1   titleType       1004 non-null   object \n",
            " 2   primaryTitle    1004 non-null   object \n",
            " 3   originalTitle   1004 non-null   object \n",
            " 4   isAdult         1004 non-null   int64  \n",
            " 5   startYear       1004 non-null   float64\n",
            " 6   endYear         17 non-null     float64\n",
            " 7   runtimeMinutes  1004 non-null   float64\n",
            " 8   genres          1004 non-null   object \n",
            " 9   averageRating   1004 non-null   float64\n",
            " 10  numVotes        1004 non-null   int64  \n",
            "dtypes: float64(4), int64(2), object(5)\n",
            "memory usage: 94.1+ KB\n",
            "None\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xpA8L7uC5t03"
      },
      "source": [
        "## Formula dari IMDB dengan Weighted Rating\n",
        "\n",
        "weighted rank (WR) = (v ÷ (v+m)) × R + (m ÷ (v+m)) × C\n",
        "\n",
        "dimana,\n",
        "\n",
        "\n",
        "*   v: jumlah votes untuk film tersebut, \n",
        "*   m: jumlah minimum votes yang dibutuhkan supaya dapat masuk dalam chart, \n",
        "*   R: rata-rata rating dari film tersebut, \n",
        "*   C: rata-rata jumlah votes dari seluruh semesta film.\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V6AU2VQ241fX",
        "outputId": "66d90dc5-e2dd-4ac0-8fc1-d4adf4e931eb"
      },
      "source": [
        "C = movie_rating_df['averageRating'].mean()\n",
        "print(C)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "6.829581673306767\n"
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
        "id": "R0rLw4tN5oMz",
        "outputId": "f9956ce3-f475-4362-d4e9-1d6ce2eb5b55"
      },
      "source": [
        "#Mengambil numVotes di atas 80% populasi\n",
        "m = movie_rating_df['numVotes'].quantile(0.8)\n",
        "print(m)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "229.0\n"
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
        "id": "jFnHXKAA5_gM",
        "outputId": "f3888260-8af1-4b40-9255-c9b9f12b9879"
      },
      "source": [
        "#Membuat Fungsi Weighted Rating\n",
        "def imdb_weighted_rating(df, var=0.8):\n",
        "    v = df['numVotes']\n",
        "    R = df['averageRating']\n",
        "    C = df['averageRating'].mean()\n",
        "    m = df['numVotes'].quantile(var)\n",
        "    df['score'] = (v/(m+v))*R + (m/(m+v))*C #Rumus IMDb \n",
        "    return df['score']\n",
        "    \n",
        "imdb_weighted_rating(movie_rating_df)\n",
        "\n",
        "#melakukan pengecekan dataframe\n",
        "print(movie_rating_df.head())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "      tconst  titleType  ... numVotes     score\n",
            "0  tt0043745      short  ...      459  7.009992\n",
            "1  tt0167491      video  ...        7  6.796077\n",
            "2  tt6574096  tvEpisode  ...      240  7.684380\n",
            "5  tt2262289      movie  ...       27  6.921384\n",
            "6  tt0874027  tvEpisode  ...        8  6.869089\n",
            "\n",
            "[5 rows x 12 columns]\n"
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
        "id": "fHcjbsDV6iIP",
        "outputId": "da3ee48a-c6e0-4da0-80ea-4c35a20cf934"
      },
      "source": [
        "#Membuat fungsi simple_recommender\n",
        "def simple_recommender(df, top=100):\n",
        "    df = df.loc[df['numVotes'] >= m] #Filter numVotes yang lebih dari m\n",
        "    df = df.sort_values(by='score', ascending=False) #urutkan dari nilai tertinggi ke terendah\n",
        "    \n",
        "    #Ambil data 100 teratas\n",
        "    df = df[:top]\n",
        "    return df\n",
        "    \n",
        "#Ambil data 25 teratas     \n",
        "print(simple_recommender(movie_rating_df, top=25))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "         tconst  titleType  ... numVotes     score\n",
            "68    tt4110822  tvEpisode  ...     3820  9.254624\n",
            "236   tt2200252      video  ...     1411  8.955045\n",
            "1181  tt7697962  tvEpisode  ...     1536  8.892450\n",
            "326   tt7124590  tvEpisode  ...     1859  8.850993\n",
            "1045  tt0533506  tvEpisode  ...     2740  8.740308\n",
            "71    tt8399426  tvEpisode  ...     1428  8.700045\n",
            "1234  tt2843830  tvEpisode  ...     1753  8.660784\n",
            "1087  tt4295140   tvSeries  ...    12056  8.566998\n",
            "1054  tt2503932  tvEpisode  ...     2495  8.451165\n",
            "448   tt0337566      video  ...     1343  8.256663\n",
            "624   tt0620159  tvEpisode  ...      401  8.020118\n",
            "1281  tt3166390  tvEpisode  ...      396  8.014679\n",
            "314   tt0954759  tvEpisode  ...     2766  8.002863\n",
            "189   tt5661506      video  ...      330  7.992798\n",
            "151   tt3954426  tvEpisode  ...      437  7.991253\n",
            "1344  tt6644294  tvEpisode  ...      812  7.976536\n",
            "1242  tt3677742  tvSpecial  ...     1931  7.965312\n",
            "1217  tt3642464  tvEpisode  ...      566  7.947641\n",
            "544   tt0734655  tvEpisode  ...     1559  7.937290\n",
            "49    tt9119838  tvEpisode  ...      263  7.936330\n",
            "357   tt4084774  tvEpisode  ...      289  7.928908\n",
            "1111  tt4174072  tvEpisode  ...     2898  7.914287\n",
            "790   tt4279086  tvEpisode  ...      823  7.901687\n",
            "972   tt0048028      movie  ...    38543  7.893678\n",
            "819   tt0032156      movie  ...     2974  7.823470\n",
            "\n",
            "[25 rows x 12 columns]\n"
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
        "id": "b4h5gpF_7G_z",
        "outputId": "ffdf77e8-8398-4344-d9e4-76ac66cd4bba"
      },
      "source": [
        "df = movie_rating_df.copy()\n",
        "\n",
        "def user_prefer_recommender(df, ask_adult, ask_start_year, ask_genre, top=100):\n",
        "    #ask_adult = yes/no\n",
        "    if ask_adult.lower() == 'yes':\n",
        "        df = df.loc[df['isAdult'] == 1]\n",
        "    elif ask_adult.lower() == 'no':\n",
        "        df = df.loc[df['isAdult'] == 0]\n",
        "\n",
        "    #ask_start_year = numeric\n",
        "    df = df.loc[df['startYear'] >= int(ask_start_year)]\n",
        "\n",
        "    #ask_genre = 'all' atau yang lain\n",
        "    if ask_genre.lower() == 'all':\n",
        "        df = df\n",
        "    else:\n",
        "        def filter_genre(x):\n",
        "            if ask_genre.lower() in str(x).lower():\n",
        "                return True\n",
        "            else:\n",
        "                return False\n",
        "        df = df.loc[df['genres'].apply(lambda x: filter_genre(x))]\n",
        "\n",
        "    df = df.loc[df['numVotes'] >= m] #Mengambil film dengan m yang lebih besar dibanding numVotes\n",
        "    df = df.sort_values(by='score', ascending=False)\n",
        "    \n",
        "    #jika kamu hanya ingin mengambil 100 teratas\n",
        "    df = df[:top]\n",
        "    return df\n",
        "\n",
        "print(user_prefer_recommender(df,\n",
        "                       ask_adult = 'no',\n",
        "                        ask_start_year = 2000,\n",
        "                       ask_genre = 'drama'\n",
        "                       ))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "         tconst  titleType  ... numVotes     score\n",
            "68    tt4110822  tvEpisode  ...     3820  9.254624\n",
            "1181  tt7697962  tvEpisode  ...     1536  8.892450\n",
            "326   tt7124590  tvEpisode  ...     1859  8.850993\n",
            "71    tt8399426  tvEpisode  ...     1428  8.700045\n",
            "1234  tt2843830  tvEpisode  ...     1753  8.660784\n",
            "1054  tt2503932  tvEpisode  ...     2495  8.451165\n",
            "1281  tt3166390  tvEpisode  ...      396  8.014679\n",
            "151   tt3954426  tvEpisode  ...      437  7.991253\n",
            "1344  tt6644294  tvEpisode  ...      812  7.976536\n",
            "357   tt4084774  tvEpisode  ...      289  7.928908\n",
            "708   tt2751234  tvEpisode  ...     1077  7.794774\n",
            "605   tt9141176  tvEpisode  ...      674  7.777823\n",
            "983   tt5063116  tvEpisode  ...      275  7.741020\n",
            "1017  tt2206822  tvEpisode  ...      525  7.644528\n",
            "73    tt0847785  tvEpisode  ...      405  7.641127\n",
            "625   tt7348490  tvEpisode  ...      413  7.518184\n",
            "1272  tt0534736  tvEpisode  ...      689  7.482870\n",
            "800   tt0901201  tvEpisode  ...      654  7.474263\n",
            "659   tt3909890  tvEpisode  ...      410  7.452229\n",
            "1170  tt0647504  tvEpisode  ...      538  7.440123\n",
            "1001  tt2129485  tvEpisode  ...      501  7.426951\n",
            "977   tt4391820  tvEpisode  ...     1558  7.414087\n",
            "1096  tt6822518      movie  ...     1541  7.413262\n",
            "910   tt3348270  tvEpisode  ...      436  7.400262\n",
            "746   tt0534765  tvEpisode  ...      620  7.392196\n",
            "299   tt4527626  tvEpisode  ...      859  7.358892\n",
            "509   tt1256301  tvEpisode  ...      501  7.358321\n",
            "897   tt2349242  tvEpisode  ...      270  7.354658\n",
            "1090  tt0212815      movie  ...     3906  7.273948\n",
            "109   tt1753383      movie  ...    61521  7.198626\n",
            "550   tt8163822      short  ...     2222  7.165391\n",
            "834   tt6509862      movie  ...      960  7.047918\n",
            "600   tt0329002      movie  ...      423  7.005022\n",
            "642   tt0993186  tvEpisode  ...     4982  6.992511\n",
            "691   tt3663996  tvEpisode  ...      309  6.927461\n",
            "727   tt3563898   tvSeries  ...      733  6.807042\n",
            "164   tt0464049      movie  ...    19858  6.800337\n",
            "893   tt8858104      movie  ...     7935  6.703635\n",
            "927   tt3663990  tvEpisode  ...      403  6.683187\n",
            "462   tt5197828  tvEpisode  ...      641  6.586752\n",
            "1068  tt8369852  tvEpisode  ...      563  6.453124\n",
            "940   tt0396190      movie  ...     2342  6.438263\n",
            "610   tt3526706      movie  ...     3890  6.329443\n",
            "1126  tt2151739      movie  ...      258  6.284136\n",
            "637   tt0857275      movie  ...     2288  6.166378\n",
            "385   tt0472259      movie  ...     3738  6.047889\n",
            "1014  tt1159705      movie  ...      355  5.899785\n",
            "1043  tt5518756      movie  ...      387  5.742978\n",
            "1154  tt1386492      movie  ...      642  5.186193\n",
            "492   tt0882806      movie  ...      229  5.164791\n",
            "922   tt2948790      movie  ...    11434  5.133960\n",
            "690   tt4477536      movie  ...    50572  4.510501\n",
            "677   tt8923408  tvEpisode  ...      592  4.500821\n",
            "1039  tt5227468      movie  ...      374  4.330305\n",
            "1138  tt1126516      movie  ...      527  4.020601\n",
            "1208  tt3044882      movie  ...     1132  3.810708\n",
            "1197  tt3016748      movie  ...     2065  3.742360\n",
            "846   tt0488164      movie  ...     1620  3.474296\n",
            "90    tt0299981    tvMovie  ...     8855  3.194020\n",
            "\n",
            "[59 rows x 12 columns]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ct-SsPAb8ddS"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
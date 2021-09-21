{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Building Recommender Function System with Similiarty Fucntion.ipynb",
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
      "cell_type": "markdown",
      "metadata": {
        "id": "enmBUKlyAqrA"
      },
      "source": [
        "## Import Basics Library and File Unloading"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jhUub7BN_UlY"
      },
      "source": [
        "#import library yang dibutuhkan\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "\n",
        "#lakukan pembacaan dataset\n",
        "movie_rating_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/movie_rating_df.csv') \n",
        "#untuk menyimpan movie_rating_df.csv\n"
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
        "id": "ykB59Zci_qHo",
        "outputId": "c471d6bb-292f-4ce3-b914-e9a624f4cc21"
      },
      "source": [
        "#tampilkan 5 baris teratas dari movive_rating_df\n",
        "print(movie_rating_df.head())\n",
        "\n",
        "#tampilkan info mengenai tipe data dari tiap kolom\n",
        "print(movie_rating_df.info())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "      tconst titleType  ... averageRating numVotes\n",
            "0  tt0000001     short  ...           5.6     1608\n",
            "1  tt0000002     short  ...           6.0      197\n",
            "2  tt0000003     short  ...           6.5     1285\n",
            "3  tt0000004     short  ...           6.1      121\n",
            "4  tt0000005     short  ...           6.1     2050\n",
            "\n",
            "[5 rows x 11 columns]\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 751614 entries, 0 to 751613\n",
            "Data columns (total 11 columns):\n",
            " #   Column          Non-Null Count   Dtype  \n",
            "---  ------          --------------   -----  \n",
            " 0   tconst          751614 non-null  object \n",
            " 1   titleType       751614 non-null  object \n",
            " 2   primaryTitle    751614 non-null  object \n",
            " 3   originalTitle   751614 non-null  object \n",
            " 4   isAdult         751614 non-null  int64  \n",
            " 5   startYear       751614 non-null  float64\n",
            " 6   endYear         16072 non-null   float64\n",
            " 7   runtimeMinutes  751614 non-null  float64\n",
            " 8   genres          486766 non-null  object \n",
            " 9   averageRating   751614 non-null  float64\n",
            " 10  numVotes        751614 non-null  int64  \n",
            "dtypes: float64(4), int64(2), object(5)\n",
            "memory usage: 63.1+ MB\n",
            "None\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "uUFIXI7SAx12"
      },
      "source": [
        "## Add Actors Dataframe\n",
        "\n",
        "Dari output yang sudah dihasilkan sebelumnya, kita dapat memperoleh list film dengan beberapa metadata seperti isAdult, runtimeMinutes, dan genres nya\n",
        "\n",
        "Selanjutnya, kita akan menambahkan metadata lain seperti aktor/aktris yang bermain di film tersebut, kita akan menggunakan dataframe lain kemudian akan melakukan join dengan dataframe movie_rating_df. "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GjOvPLt1AByz",
        "outputId": "6eb6bcbc-7c3c-4ece-c240-2c263107c4cf"
      },
      "source": [
        "#Simpan actor_name.csv pada variable name_df \n",
        "name_df = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/actor_name.csv')\n",
        "\n",
        "#Tampilkan 5 baris teratas dari name_df\n",
        "print(name_df.head())\n",
        "\n",
        "#Tampilkan informasi mengenai tipe data dari tiap kolom pada name_df\n",
        "print(name_df.info())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "       nconst  ...                           knownForTitles\n",
            "0   nm1774132  ...  tt0417686,tt1713976,tt1891860,tt0454839\n",
            "1  nm10683464  ...                                tt7718088\n",
            "2   nm1021485  ...                                tt0168790\n",
            "3   nm6940929  ...                                tt4232168\n",
            "4   nm5764974  ...                                tt3014168\n",
            "\n",
            "[5 rows x 6 columns]\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 1000 entries, 0 to 999\n",
            "Data columns (total 6 columns):\n",
            " #   Column             Non-Null Count  Dtype \n",
            "---  ------             --------------  ----- \n",
            " 0   nconst             1000 non-null   object\n",
            " 1   primaryName        1000 non-null   object\n",
            " 2   birthYear          1000 non-null   object\n",
            " 3   deathYear          1000 non-null   object\n",
            " 4   primaryProfession  891 non-null    object\n",
            " 5   knownForTitles     1000 non-null   object\n",
            "dtypes: object(6)\n",
            "memory usage: 47.0+ KB\n",
            "None\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "B4Wby_iUBC9A"
      },
      "source": [
        "## Add Directors and Writers Dataframe\n",
        "\n",
        "Dataframe yang akan ditambahkan selanjutnya adalah dataframe yang berisi directors dan writers dari film."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XEQFyFCxArMY",
        "outputId": "696d71bb-5739-4ce0-ec5c-f24893d6a30c"
      },
      "source": [
        "#Menyimpan dataset pada variabel director_writers\n",
        "director_writers = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/directors_writers.csv')\n",
        "\n",
        "#Manampilkan 5 baris teratas\n",
        "print(director_writers.head())\n",
        "\n",
        "#Menampilkan informasi tipe data\n",
        "print(director_writers.info())\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "      tconst  ...                                      writer_name\n",
            "0  tt0011414  ...                          John Emerson,Anita Loos\n",
            "1  tt0011890  ...     Arthur F. Goodrich,Burns Mantle,Mary Murillo\n",
            "2  tt0014341  ...  Jean C. Havez,Clyde Bruckman,Joseph A. Mitchell\n",
            "3  tt0018054  ...                                Jeanie Macpherson\n",
            "4  tt0024151  ...                 Max Miller,Wells Root,Jack Jevne\n",
            "\n",
            "[5 rows x 3 columns]\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 986 entries, 0 to 985\n",
            "Data columns (total 3 columns):\n",
            " #   Column         Non-Null Count  Dtype \n",
            "---  ------         --------------  ----- \n",
            " 0   tconst         986 non-null    object\n",
            " 1   director_name  986 non-null    object\n",
            " 2   writer_name    986 non-null    object\n",
            "dtypes: object(3)\n",
            "memory usage: 23.2+ KB\n",
            "None\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "h1wT7X2-BfOE"
      },
      "source": [
        "## Convert into List\n",
        "\n",
        "Setelah menampilkan informasi mengenai dataframe directors_writer, dapat dilihat bahwa tidak ada nilai NULL pada dataset tersebut. Hal selanjutnya yang akan kita lakukan adalah mengubah director_name dan writer_name dari string menjadi list"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6q5wP3MDBjvQ",
        "outputId": "256a5bb4-b0fd-4202-c9d0-aafb88f817c9"
      },
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "#mengubah director_name dan writer_name dari string menjadi list\n",
        "director_writers = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/directors_writers.csv')\n",
        "\n",
        "#Mengubah director_name menjadi list\n",
        "director_writers['director_name'] = director_writers['director_name'].apply(lambda row: row.split(','))\n",
        "director_writers['writer_name'] = director_writers['writer_name'].apply(lambda row: row.split(','))\n",
        "\n",
        "#Tampilkan 5 data teratas\n",
        "print(director_writers.head())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "      tconst  ...                                        writer_name\n",
            "0  tt0011414  ...                         [John Emerson, Anita Loos]\n",
            "1  tt0011890  ...   [Arthur F. Goodrich, Burns Mantle, Mary Murillo]\n",
            "2  tt0014341  ...  [Jean C. Havez, Clyde Bruckman, Joseph A. Mitc...\n",
            "3  tt0018054  ...                                [Jeanie Macpherson]\n",
            "4  tt0024151  ...               [Max Miller, Wells Root, Jack Jevne]\n",
            "\n",
            "[5 rows x 3 columns]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HAIyLxLnAGij"
      },
      "source": [
        "## Update name_df\n",
        "\n",
        "Kita hanya akan membutuhkan kolom nconst, primaryName, dan knownForTitles pada name_df untuk mencocokkan aktor/aktris ini dengan film yang ada."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Cw2D4j61DVhV",
        "outputId": "f053e8bf-b54f-4d14-ecec-26c5d0e6de0b"
      },
      "source": [
        "#Update name_df\n",
        "name_df = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/actor_name.csv')\n",
        "#Kita hanya akan membutuhkan kolom nconst, primaryName, dan knownForTitles\n",
        "name_df = name_df[['nconst','primaryName','knownForTitles']]\n",
        "\n",
        "#Tampilkan 5 baris teratas dari name_df\n",
        "print(name_df.head())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "       nconst          primaryName                           knownForTitles\n",
            "0   nm1774132    Nathan McLaughlin  tt0417686,tt1713976,tt1891860,tt0454839\n",
            "1  nm10683464        Bridge Andrew                                tt7718088\n",
            "2   nm1021485    Brandon Fransvaag                                tt0168790\n",
            "3   nm6940929   Erwin van der Lely                                tt4232168\n",
            "4   nm5764974  Svetlana Shypitsyna                                tt3014168\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rPWd8AUwANKu"
      },
      "source": [
        "## Movies per Actor\n",
        "\n",
        "kita ketahui adalah mengenai variasi dari jumlah film yang dapat dibintangi oleh seorang aktor.\n",
        "\n",
        "Tentunya seorang aktor dapat membintangi lebih dari 1 film, bukan? maka akan diperlukan untuk membuat table yang mempunyai relasi 1-1 ke masing-masing title movie tersebut. Kita akan melakukan unnest terhadap table tersebut. \n",
        "\n",
        "\n",
        "1.   Melakukan pengecekan variasi jumlah film yang dibintangi oleh aktor.\n",
        "2.   Mengubah kolom 'knownForTitles' menjadi list of list.\n",
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
        "id": "am0qVJxR7jOc",
        "outputId": "24ef7542-b945-4959-b7e4-6347c98e00e1"
      },
      "source": [
        "#Melakukan pengecekan variasi\n",
        "print(name_df['knownForTitles'].apply(lambda x: len(x.split(','))).unique())\n",
        "\n",
        "#Mengubah knownForTitles menjadi list of list\n",
        "name_df['knownForTitles'] = name_df['knownForTitles'].apply(lambda x: x.split(','))\n",
        "\n",
        "#Mencetak 5 baris teratas\n",
        "print(name_df.head())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[4 1 2 3]\n",
            "       nconst  ...                                knownForTitles\n",
            "0   nm1774132  ...  [tt0417686, tt1713976, tt1891860, tt0454839]\n",
            "1  nm10683464  ...                                   [tt7718088]\n",
            "2   nm1021485  ...                                   [tt0168790]\n",
            "3   nm6940929  ...                                   [tt4232168]\n",
            "4   nm5764974  ...                                   [tt3014168]\n",
            "\n",
            "[5 rows x 3 columns]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iIS_BcbyAf-B"
      },
      "source": [
        "## Korespondensi 1 - 1\n",
        "\n",
        "Karena pada data sebelumnya dapat dilihat bahwa seorang aktor dapat membintangi 1 sampai 4 film, diperlukan untuk membuat table yang mempunyai relasi 1-1 dari aktor ke masing-masing title movie tersebut"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "palV6dgU8Qff",
        "outputId": "e21434c6-9d51-47fb-966f-ecc3f5ae8747"
      },
      "source": [
        "import numpy as np\n",
        "#menyiapkan bucket untuk dataframe\n",
        "df_uni = []\n",
        "\n",
        "for x in ['knownForTitles']:\n",
        "    #mengulang index dari tiap baris sampai tiap elemen dari knownForTitles\n",
        "    idx = name_df.index.repeat(name_df['knownForTitles'].str.len())\n",
        "   \n",
        "   #memecah values dari list di setiap baris dan menggabungkan nya dengan rows lain menjadi dataframe\n",
        "    df1 = pd.DataFrame({\n",
        "        x: np.concatenate(name_df[x].values)\n",
        "    })\n",
        "    \n",
        "    #mengganti index dataframe tersebut dengan idx yang sudah kita define di awal\n",
        "    df1.index = idx\n",
        "    #untuk setiap dataframe yang terbentuk, kita append ke dataframe bucket\n",
        "    df_uni.append(df1)\n",
        "    \n",
        "#menggabungkan semua dataframe menjadi satu\n",
        "df_concat = pd.concat(df_uni, axis=1)\n",
        "\n",
        "#left join dengan value dari dataframe yang awal\n",
        "unnested_df = df_concat.join(name_df.drop(['knownForTitles'], 1), how='left')\n",
        "\n",
        "#select kolom sesuai dengan dataframe awal\n",
        "unnested_df = unnested_df[name_df.columns.tolist()]\n",
        "print(unnested_df)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "         nconst        primaryName knownForTitles\n",
            "0     nm1774132  Nathan McLaughlin      tt0417686\n",
            "0     nm1774132  Nathan McLaughlin      tt1713976\n",
            "0     nm1774132  Nathan McLaughlin      tt1891860\n",
            "0     nm1774132  Nathan McLaughlin      tt0454839\n",
            "1    nm10683464      Bridge Andrew      tt7718088\n",
            "..          ...                ...            ...\n",
            "998   nm5245804      Eliza Jenkins      tt1464058\n",
            "999   nm0948460         Greg Yolen      tt0436869\n",
            "999   nm0948460         Greg Yolen      tt0476663\n",
            "999   nm0948460         Greg Yolen      tt0109723\n",
            "999   nm0948460         Greg Yolen      tt0364484\n",
            "\n",
            "[1918 rows x 3 columns]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "l0JfAVedAozE"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QehBIel__u0I"
      },
      "source": [
        "## Mengelompokkan primaryName menjadi list group by knownForTitles\n",
        "\n",
        "Kita akan melakukan grouping kembali pada kolom player karena yang kita inginkan adalah level movie untuk melakukan movie recommendation"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mfWMTRkk9Ekk",
        "outputId": "aef7569d-3e23-40f0-8f46-fc826992e938"
      },
      "source": [
        "unnested_drop = unnested_df.drop(['nconst'], axis=1)\n",
        "\n",
        "#menyiapkan bucket untuk dataframe\n",
        "df_uni = []\n",
        "\n",
        "for col in ['primaryName']:\n",
        "    #agregasi kolom PrimaryName sesuai group_col yang sudah di define di atas\n",
        "    dfi = unnested_drop.groupby(['knownForTitles'])[col].apply(list)\n",
        "    #Lakukan append\n",
        "    df_uni.append(dfi)\n",
        "df_grouped = pd.concat(df_uni, axis=1).reset_index()\n",
        "df_grouped.columns = ['knownForTitles','cast_name']\n",
        "print(df_grouped)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "     knownForTitles           cast_name\n",
            "0         tt0008125    [Charles Harley]\n",
            "1         tt0009706    [Charles Harley]\n",
            "2         tt0010304  [Natalie Talmadge]\n",
            "3         tt0011414  [Natalie Talmadge]\n",
            "4         tt0011890  [Natalie Talmadge]\n",
            "...             ...                 ...\n",
            "1893      tt9610496  [Stefano Baffetti]\n",
            "1894      tt9714030        [Kevin Kain]\n",
            "1895      tt9741820   [Caroline Plyler]\n",
            "1896      tt9759814     [Ethan Francis]\n",
            "1897      tt9856236     [Nuala Maguire]\n",
            "\n",
            "[1898 rows x 2 columns]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wDJKsD-aBvAC"
      },
      "source": [
        "## Join table\n",
        "\n",
        "\n",
        "\n",
        "*   join antara movie table dan cast table  ( field knownForTitles dan tconst)\n",
        "*   join antara base_df dengan director_writer table (field tconst dan tconst)\n",
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
        "id": "4AtfLHFH9hkP",
        "outputId": "dfd14177-187b-458f-f32f-139ac8a1aa65"
      },
      "source": [
        "movie_rating_df = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/movie_rating_df.csv')\n",
        "\n",
        "#join antara movie table dan cast table \n",
        "base_df = pd.merge(df_grouped, movie_rating_df, left_on='knownForTitles', right_on='tconst', how='inner')\n",
        "\n",
        "#join antara base_df dengan director_writer table\n",
        "base_df = pd.merge(base_df, director_writers, left_on='tconst', right_on='tconst', how='left')\n",
        "print(base_df.head())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "  knownForTitles  ...                                        writer_name\n",
            "0      tt0011414  ...                         [John Emerson, Anita Loos]\n",
            "1      tt0011890  ...   [Arthur F. Goodrich, Burns Mantle, Mary Murillo]\n",
            "2      tt0014341  ...  [Jean C. Havez, Clyde Bruckman, Joseph A. Mitc...\n",
            "3      tt0018054  ...                                [Jeanie Macpherson]\n",
            "4      tt0024151  ...               [Max Miller, Wells Root, Jack Jevne]\n",
            "\n",
            "[5 rows x 15 columns]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UgUaIPGAB9MO"
      },
      "source": [
        "## Cleaning data\n",
        "\n",
        "Setelah melakukan join table sebelumnya, sekarang hal yang akan kembali kita lakukan adalah melakukan cleaning pada data yang sudah dihasilkan. "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A0Dqx4-q96qZ",
        "outputId": "7b2f5b59-e12d-4b80-a70a-b969a55b191b"
      },
      "source": [
        "#Melakukan drop terhadap kolom knownForTitles\n",
        "base_drop = base_df.drop(['knownForTitles'], axis=1)\n",
        "print(base_drop.info())\n",
        "\n",
        "#Mengganti nilai NULL pada kolom genres dengan 'Unknown'\n",
        "base_drop['genres'] = base_drop['genres'].fillna('Unknown')\n",
        "\n",
        "#Melakukan perhitungan jumlah nilai NULL pada tiap kolom\n",
        "print(base_drop.isnull().sum())\n",
        "\n",
        "#Mengganti nilai NULL pada kolom dorector_name dan writer_name dengan 'Unknown'\n",
        "base_drop[['director_name','writer_name']] = base_drop[['director_name','writer_name']].fillna('unknown')\n",
        "\n",
        "#karena value kolom genres terdapat multiple values, jadi kita akan bungkus menjadi list of list\n",
        "base_drop['genres'] = base_drop['genres'].apply(lambda x: x.split(','))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Int64Index: 1060 entries, 0 to 1059\n",
            "Data columns (total 14 columns):\n",
            " #   Column          Non-Null Count  Dtype  \n",
            "---  ------          --------------  -----  \n",
            " 0   cast_name       1060 non-null   object \n",
            " 1   tconst          1060 non-null   object \n",
            " 2   titleType       1060 non-null   object \n",
            " 3   primaryTitle    1060 non-null   object \n",
            " 4   originalTitle   1060 non-null   object \n",
            " 5   isAdult         1060 non-null   int64  \n",
            " 6   startYear       1060 non-null   float64\n",
            " 7   endYear         110 non-null    float64\n",
            " 8   runtimeMinutes  1060 non-null   float64\n",
            " 9   genres          745 non-null    object \n",
            " 10  averageRating   1060 non-null   float64\n",
            " 11  numVotes        1060 non-null   int64  \n",
            " 12  director_name   986 non-null    object \n",
            " 13  writer_name     986 non-null    object \n",
            "dtypes: float64(4), int64(2), object(8)\n",
            "memory usage: 124.2+ KB\n",
            "None\n",
            "cast_name           0\n",
            "tconst              0\n",
            "titleType           0\n",
            "primaryTitle        0\n",
            "originalTitle       0\n",
            "isAdult             0\n",
            "startYear           0\n",
            "endYear           950\n",
            "runtimeMinutes      0\n",
            "genres              0\n",
            "averageRating       0\n",
            "numVotes            0\n",
            "director_name      74\n",
            "writer_name        74\n",
            "dtype: int64\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IaiRITA2-5xL"
      },
      "source": [
        "## Reformat table base_df\n",
        "\n",
        "\n",
        "\n",
        "*   Item daftar\n",
        "\n",
        "*   primaryTitle -> title\n",
        "*   titleType -> type\n",
        "*   Item daftar\n",
        "*   startYear -> start\n",
        "*   runtimeMinutes -> duration\n",
        "*   averageRating -> rating\n",
        "*   numVotes -> votes\n",
        "\n",
        "\n",
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
        "id": "_EtVNTPK-YWA",
        "outputId": "c566f68e-d113-48fd-d9fd-b19d6b56a986"
      },
      "source": [
        "#Drop kolom tconst, isAdult, endYear, originalTitle\n",
        "base_drop2 = base_drop.drop(['tconst','isAdult','endYear','originalTitle'], axis=1)\n",
        "base_drop2 = base_drop2[['primaryTitle','titleType','startYear','runtimeMinutes','genres','averageRating','numVotes','cast_name','director_name','writer_name']]\n",
        "\n",
        "# Gunakan petunjuk!\n",
        "base_drop2.columns = ['title','type','start','duration','genres','rating','votes','cast_name','director_name','writer_name']\n",
        "print(base_drop2.head())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "                    title  ...                                        writer_name\n",
            "0         The Love Expert  ...                         [John Emerson, Anita Loos]\n",
            "1               Yes or No  ...   [Arthur F. Goodrich, Burns Mantle, Mary Murillo]\n",
            "2         Our Hospitality  ...  [Jean C. Havez, Clyde Bruckman, Joseph A. Mitc...\n",
            "3       The King of Kings  ...                                [Jeanie Macpherson]\n",
            "4  I Cover the Waterfront  ...               [Max Miller, Wells Root, Jack Jevne]\n",
            "\n",
            "[5 rows x 10 columns]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rE2_xt5n_dYw"
      },
      "source": [
        "## Klasifikasi Metadata"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OwZaHVcJ-4lu",
        "outputId": "dd899314-3d44-4b65-b959-250102446cbd"
      },
      "source": [
        "#Klasifikasi berdasar title, cast_name, genres, director_name, dan writer_name\n",
        "feature_df = base_drop2[['title','cast_name','genres','director_name','writer_name']]\n",
        "\n",
        "#Tampilkan 5 baris teratas\n",
        "print(feature_df.head())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "                    title  ...                                        writer_name\n",
            "0         The Love Expert  ...                         [John Emerson, Anita Loos]\n",
            "1               Yes or No  ...   [Arthur F. Goodrich, Burns Mantle, Mary Murillo]\n",
            "2         Our Hospitality  ...  [Jean C. Havez, Clyde Bruckman, Joseph A. Mitc...\n",
            "3       The King of Kings  ...                                [Jeanie Macpherson]\n",
            "4  I Cover the Waterfront  ...               [Max Miller, Wells Root, Jack Jevne]\n",
            "\n",
            "[5 rows x 5 columns]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zpJpYPR5jMzC"
      },
      "source": [
        "## Bagaimana cara membuat fungsi untuk strip spaces dari setiap row dan setiap elemennya?"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b65wkzOSjs9M",
        "outputId": "827c397a-fc17-448f-b609-4077054794e1"
      },
      "source": [
        "def sanitize(x):\n",
        "    try:\n",
        "        #kalau cell berisi list\n",
        "        if isinstance(x,list):\n",
        "            return [i.replace(' ','').lower() for i in x]\n",
        "        #kalau cell berisi string\n",
        "        else:\n",
        "            return [x.replace(' ','').lower()]\n",
        "    except:\n",
        "        print(x)\n",
        "        \n",
        "#Kolom : cast_name, genres, writer_name, director_name        \n",
        "feature_cols = ['cast_name','genres','writer_name','director_name']\n",
        "\n",
        "#Apply function sanitize \n",
        "for col in feature_cols:\n",
        "    feature_df[col] = feature_df[col].apply(sanitize)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:17: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame.\n",
            "Try using .loc[row_indexer,col_indexer] = value instead\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_bok-nK3jtVo"
      },
      "source": [
        "## Bagaimana cara membuat fungsi untuk membuat metadata soup (menggabungkan semua feature menjadi 1 bagian kalimat) untuk setiap judulnya?"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mgzdXgHbioOU",
        "outputId": "4379a3ab-097c-4b75-98b6-4881cd842e15"
      },
      "source": [
        "#kolom yang digunakan : cast_name, genres, director_name, writer_name\n",
        "def soup_feature(x):\n",
        "    return ' '.join(x['cast_name']) + ' ' + ' '.join(x['genres']) + ' ' + ' '.join(x['director_name']) + ' ' + ' '.join(x['writer_name'])\n",
        "\n",
        "#membuat soup menjadi 1 kolom \n",
        "feature_df['soup'] = feature_df.apply(soup_feature, axis=1)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:6: SettingWithCopyWarning: \n",
            "A value is trying to be set on a copy of a slice from a DataFrame.\n",
            "Try using .loc[row_indexer,col_indexer] = value instead\n",
            "\n",
            "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
            "  \n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6bgT25qTkacn"
      },
      "source": [
        "## Cara menyiapkan CountVectorizer (stop_words = english) dan fit dengan soup yang kita buat di atas\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aLky1fQcj34C",
        "outputId": "4d7a06a9-5389-406f-da24-e778f6f971fd"
      },
      "source": [
        "#import CountVectorizer \n",
        "from sklearn.feature_extraction.text import CountVectorizer\n",
        "\n",
        "#definisikan CountVectorizer dan mengubah soup tadi menjadi bentuk vector\n",
        "count = CountVectorizer(stop_words='english')\n",
        "count_matrix = count.fit_transform(feature_df['soup'])\n",
        "\n",
        "print(count)\n",
        "print(count_matrix.shape)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "CountVectorizer(analyzer='word', binary=False, decode_error='strict',\n",
            "                dtype=<class 'numpy.int64'>, encoding='utf-8', input='content',\n",
            "                lowercase=True, max_df=1.0, max_features=None, min_df=1,\n",
            "                ngram_range=(1, 1), preprocessor=None, stop_words='english',\n",
            "                strip_accents=None, token_pattern='(?u)\\\\b\\\\w\\\\w+\\\\b',\n",
            "                tokenizer=None, vocabulary=None)\n",
            "(1060, 10026)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6gNnu2OMlAB1"
      },
      "source": [
        "## Cara membuat model similarity antara count matrix"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "snEb8KgiktZt",
        "outputId": "1eed8797-7ff3-4f71-a7e2-ddaf2004e21e"
      },
      "source": [
        "#Import cosine_similarity\n",
        "from sklearn.metrics.pairwise import cosine_similarity\n",
        "\n",
        "#Gunakan cosine_similarity antara count_matrix \n",
        "cosine_sim = cosine_similarity(count_matrix, count_matrix)\n",
        "\n",
        "#print hasilnya\n",
        "print(cosine_sim)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[1.         0.15430335 0.35355339 ... 0.         0.         0.13608276]\n",
            " [0.15430335 1.         0.10910895 ... 0.         0.         0.        ]\n",
            " [0.35355339 0.10910895 1.         ... 0.         0.08703883 0.09622504]\n",
            " ...\n",
            " [0.         0.         0.         ... 1.         0.         0.        ]\n",
            " [0.         0.         0.08703883 ... 0.         1.         0.10050378]\n",
            " [0.13608276 0.         0.09622504 ... 0.         0.10050378 1.        ]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cF7rWfFMlL5Z"
      },
      "source": [
        "## Cara membuat content based recommender system\n",
        "\n",
        "Task selanjutnya yang harus dilakukan adalah reverse mapping dengan judul sebagai index nya"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Pz3sp0XHe01k"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EFjbQWHBlG1J",
        "outputId": "f612f744-62b0-4b98-ec59-5c76e8ea3b16"
      },
      "source": [
        "indices = pd.Series(feature_df.index, index=feature_df['title']).drop_duplicates()\n",
        "\n",
        "def content_recommender(title):\n",
        "    #mendapatkan index dari judul film (title) yang disebutkan\n",
        "    idx = indices[title]\n",
        "\n",
        "    #menjadikan list dari array similarity cosine sim \n",
        "    #hint: cosine_sim[idx]\n",
        "    sim_scores = list(enumerate(cosine_sim[idx]))\n",
        "\n",
        "    #mengurutkan film dari similarity tertinggi ke terendah\n",
        "    sim_scores = sorted(sim_scores,key=lambda x:x[1],reverse=True)\n",
        "\n",
        "    #untuk mendapatkan list judul dari item kedua sampe ke 11\n",
        "    sim_scores = sim_scores[1:11]\n",
        "\n",
        "    #mendapatkan index dari judul-judul yang muncul di sim_scores\n",
        "    movie_indices = [i[0] for i in sim_scores]\n",
        "\n",
        "    #dengan menggunakan iloc, kita bisa panggil balik berdasarkan index dari movie_indices\n",
        "    return base_df.iloc[movie_indices]\n",
        "\n",
        "#aplikasikan function di atas\n",
        "print(content_recommender('The Lion King'))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "     knownForTitles  ...                                        writer_name\n",
            "848       tt3040964  ...                    [Justin Marks, Rudyard Kipling]\n",
            "383       tt0286336  ...  [Valerie Georgeson, Colin Dann, Jenny McDade, ...\n",
            "1002      tt7222086  ...  [Akihito Tsukushi, Keigo Koyanagi, Hideyuki Ku...\n",
            "73        tt0075147  ...                                    [James Goldman]\n",
            "232       tt0119051  ...                                      [David Mamet]\n",
            "556      tt10068158  ...                                 [Akihito Tsukushi]\n",
            "9         tt0028657  ...                    [Frances Guihan, Forrest Brown]\n",
            "191       tt0107875  ...                    [Robin Lyons, George MacDonald]\n",
            "803       tt2356464  ...         [Kristina Magdalena Henn, Lea Schmidbauer]\n",
            "983       tt6270328  ...  [David Witt, John Derevlany, David Evans, Pete...\n",
            "\n",
            "[10 rows x 15 columns]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WPwWASXUlXnw"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
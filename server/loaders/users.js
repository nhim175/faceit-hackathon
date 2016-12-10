const users = [
  {
    username: 'admin',
    email: 'admin@test.com',
    password: 'supersecret'
  },
  {
    username: 'testuser',
    email: 'test@test.com',
    password: 'testpassword'
  },
  {
    "username": "lazyfrog155",
    "email": "pilar.ortiz@example.com",
    "password": "solitude",
    "profile": {
      "name": "pilar",
      "avatar": "https://randomuser.me/api/portraits/women/82.jpg"
    }
  },
  {
    "username": "crazyladybug469",
    "email": "dionira.viana@example.com",
    "password": "ernesto",
    "profile": {
      "name": "dionira",
      "avatar": "https://randomuser.me/api/portraits/women/66.jpg"
    }
  },
  {
    "username": "redbird866",
    "email": "jamie.rose@example.com",
    "password": "trash",
    "profile": {
      "name": "jamie",
      "avatar": "https://randomuser.me/api/portraits/men/88.jpg"
    }
  },
  {
    "username": "blueswan788",
    "email": "shane.gibson@example.com",
    "password": "hearts",
    "profile": {
      "name": "shane",
      "avatar": "https://randomuser.me/api/portraits/men/83.jpg"
    }
  },
  {
    "username": "orangemouse433",
    "email": "hanaé.fabre@example.com",
    "password": "musica",
    "profile": {
      "name": "hanaé",
      "avatar": "https://randomuser.me/api/portraits/women/3.jpg"
    }
  },
  {
    "username": "silverbird172",
    "email": "ken.palmer@example.com",
    "password": "emmanuel",
    "profile": {
      "name": "ken",
      "avatar": "https://randomuser.me/api/portraits/men/32.jpg"
    }
  },
  {
    "username": "goldenmeercat566",
    "email": "peter.bishop@example.com",
    "password": "olivier",
    "profile": {
      "name": "peter",
      "avatar": "https://randomuser.me/api/portraits/men/47.jpg"
    }
  },
  {
    "username": "silvercat604",
    "email": "reginald.clarke@example.com",
    "password": "cook",
    "profile": {
      "name": "reginald",
      "avatar": "https://randomuser.me/api/portraits/men/30.jpg"
    }
  },
  {
    "username": "whiteelephant532",
    "email": "florent.garnier@example.com",
    "password": "studly",
    "profile": {
      "name": "florent",
      "avatar": "https://randomuser.me/api/portraits/men/70.jpg"
    }
  },
  {
    "username": "beautifulelephant862",
    "email": "joseph.larson@example.com",
    "password": "simone",
    "profile": {
      "name": "joseph",
      "avatar": "https://randomuser.me/api/portraits/men/71.jpg"
    }
  },
  {
    "username": "greenpanda882",
    "email": "kayla.hughes@example.com",
    "password": "labrador",
    "profile": {
      "name": "kayla",
      "avatar": "https://randomuser.me/api/portraits/women/1.jpg"
    }
  },
  {
    "username": "ticklishgorilla444",
    "email": "soline.blanc@example.com",
    "password": "54321",
    "profile": {
      "name": "soline",
      "avatar": "https://randomuser.me/api/portraits/women/5.jpg"
    }
  },
  {
    "username": "silverrabbit946",
    "email": "nadya.vantussenbroek@example.com",
    "password": "trinity",
    "profile": {
      "name": "nadya",
      "avatar": "https://randomuser.me/api/portraits/women/26.jpg"
    }
  },
  {
    "username": "goldenelephant710",
    "email": "yosra.oostdam@example.com",
    "password": "glennwei",
    "profile": {
      "name": "yosra",
      "avatar": "https://randomuser.me/api/portraits/women/73.jpg"
    }
  },
  {
    "username": "beautifulleopard220",
    "email": "matias.luoma@example.com",
    "password": "otis",
    "profile": {
      "name": "matias",
      "avatar": "https://randomuser.me/api/portraits/men/39.jpg"
    }
  },
  {
    "username": "organiccat351",
    "email": "anthony.williams@example.com",
    "password": "hannibal",
    "profile": {
      "name": "anthony",
      "avatar": "https://randomuser.me/api/portraits/men/98.jpg"
    }
  },
  {
    "username": "beautifulbutterfly528",
    "email": "montserrat.benitez@example.com",
    "password": "finance",
    "profile": {
      "name": "montserrat",
      "avatar": "https://randomuser.me/api/portraits/women/91.jpg"
    }
  },
  {
    "username": "beautifulgorilla905",
    "email": "stella.horton@example.com",
    "password": "ladder",
    "profile": {
      "name": "stella",
      "avatar": "https://randomuser.me/api/portraits/women/14.jpg"
    }
  },
  {
    "username": "beautifulostrich524",
    "email": "annie.gilbert@example.com",
    "password": "byteme",
    "profile": {
      "name": "annie",
      "avatar": "https://randomuser.me/api/portraits/women/55.jpg"
    }
  },
  {
    "username": "redladybug940",
    "email": "esma.poçan@example.com",
    "password": "xxxxxx1",
    "profile": {
      "name": "esma",
      "avatar": "https://randomuser.me/api/portraits/women/93.jpg"
    }
  },
  {
    "username": "beautifulrabbit630",
    "email": "gül.dağlaroğlu@example.com",
    "password": "sander",
    "profile": {
      "name": "gül",
      "avatar": "https://randomuser.me/api/portraits/women/46.jpg"
    }
  },
  {
    "username": "ticklishcat392",
    "email": "derrick.smith@example.com",
    "password": "josephin",
    "profile": {
      "name": "derrick",
      "avatar": "https://randomuser.me/api/portraits/men/25.jpg"
    }
  },
  {
    "username": "brownbird429",
    "email": "zilla.hogeweg@example.com",
    "password": "nineinch",
    "profile": {
      "name": "zilla",
      "avatar": "https://randomuser.me/api/portraits/women/35.jpg"
    }
  },
  {
    "username": "crazybear148",
    "email": "orêncio.souza@example.com",
    "password": "nong",
    "profile": {
      "name": "orêncio",
      "avatar": "https://randomuser.me/api/portraits/men/9.jpg"
    }
  },
  {
    "username": "lazyleopard303",
    "email": "daya.prevoo@example.com",
    "password": "italy",
    "profile": {
      "name": "daya",
      "avatar": "https://randomuser.me/api/portraits/women/22.jpg"
    }
  },
  {
    "username": "yellowdog272",
    "email": "léonie.roux@example.com",
    "password": "gertrude",
    "profile": {
      "name": "léonie",
      "avatar": "https://randomuser.me/api/portraits/women/92.jpg"
    }
  },
  {
    "username": "crazytiger256",
    "email": "sofia.pedersen@example.com",
    "password": "retired",
    "profile": {
      "name": "sofia",
      "avatar": "https://randomuser.me/api/portraits/women/84.jpg"
    }
  },
  {
    "username": "heavyfish863",
    "email": "nurdan.tunçeri@example.com",
    "password": "anthony",
    "profile": {
      "name": "nurdan",
      "avatar": "https://randomuser.me/api/portraits/women/41.jpg"
    }
  },
  {
    "username": "purplebutterfly844",
    "email": "kiara.brun@example.com",
    "password": "hair",
    "profile": {
      "name": "kiara",
      "avatar": "https://randomuser.me/api/portraits/women/84.jpg"
    }
  },
  {
    "username": "browngoose518",
    "email": "carter.chen@example.com",
    "password": "taylor1",
    "profile": {
      "name": "carter",
      "avatar": "https://randomuser.me/api/portraits/men/63.jpg"
    }
  },
  {
    "username": "beautifulfrog619",
    "email": "florian.dupont@example.com",
    "password": "arcadia",
    "profile": {
      "name": "florian",
      "avatar": "https://randomuser.me/api/portraits/men/51.jpg"
    }
  },
  {
    "username": "blacklion446",
    "email": "cléa.riviere@example.com",
    "password": "milano",
    "profile": {
      "name": "cléa",
      "avatar": "https://randomuser.me/api/portraits/women/28.jpg"
    }
  },
  {
    "username": "bigsnake281",
    "email": "david.lam@example.com",
    "password": "12345",
    "profile": {
      "name": "david",
      "avatar": "https://randomuser.me/api/portraits/men/4.jpg"
    }
  },
  {
    "username": "blackbear954",
    "email": "henri.strauß@example.com",
    "password": "lalala",
    "profile": {
      "name": "henri",
      "avatar": "https://randomuser.me/api/portraits/men/18.jpg"
    }
  },
  {
    "username": "bigcat672",
    "email": "melodie.mackay@example.com",
    "password": "dragonfl",
    "profile": {
      "name": "melodie",
      "avatar": "https://randomuser.me/api/portraits/women/5.jpg"
    }
  },
  {
    "username": "bluemouse447",
    "email": "tude.daconceição@example.com",
    "password": "wapapapa",
    "profile": {
      "name": "tude",
      "avatar": "https://randomuser.me/api/portraits/men/22.jpg"
    }
  },
  {
    "username": "heavygorilla246",
    "email": "coşkun.gürmen@example.com",
    "password": "card",
    "profile": {
      "name": "coşkun",
      "avatar": "https://randomuser.me/api/portraits/men/2.jpg"
    }
  },
  {
    "username": "silversnake611",
    "email": "eliza.reed@example.com",
    "password": "success1",
    "profile": {
      "name": "eliza",
      "avatar": "https://randomuser.me/api/portraits/women/93.jpg"
    }
  },
  {
    "username": "silverkoala585",
    "email": "jessica.hamilton@example.com",
    "password": "rivers",
    "profile": {
      "name": "jessica",
      "avatar": "https://randomuser.me/api/portraits/women/9.jpg"
    }
  },
  {
    "username": "bigmeercat199",
    "email": "clarence.wood@example.com",
    "password": "berlin",
    "profile": {
      "name": "clarence",
      "avatar": "https://randomuser.me/api/portraits/men/23.jpg"
    }
  },
  {
    "username": "tinyfrog833",
    "email": "sofia.hansen@example.com",
    "password": "melissa1",
    "profile": {
      "name": "sofia",
      "avatar": "https://randomuser.me/api/portraits/women/41.jpg"
    }
  },
  {
    "username": "browngorilla130",
    "email": "amrish.bernard@example.com",
    "password": "meadow",
    "profile": {
      "name": "amrish",
      "avatar": "https://randomuser.me/api/portraits/men/35.jpg"
    }
  },
  {
    "username": "bigswan506",
    "email": "juan.vidal@example.com",
    "password": "driver",
    "profile": {
      "name": "juan",
      "avatar": "https://randomuser.me/api/portraits/men/86.jpg"
    }
  },
  {
    "username": "redbear426",
    "email": "محمدامين.حیدری@example.com",
    "password": "rang",
    "profile": {
      "name": "محمدامين",
      "avatar": "https://randomuser.me/api/portraits/men/23.jpg"
    }
  },
  {
    "username": "silverswan131",
    "email": "zachary.walker@example.com",
    "password": "space",
    "profile": {
      "name": "zachary",
      "avatar": "https://randomuser.me/api/portraits/men/99.jpg"
    }
  },
  {
    "username": "greenmouse659",
    "email": "ferry.schep@example.com",
    "password": "nylons",
    "profile": {
      "name": "ferry",
      "avatar": "https://randomuser.me/api/portraits/men/21.jpg"
    }
  },
  {
    "username": "whitepanda354",
    "email": "lilja.haapala@example.com",
    "password": "kendall",
    "profile": {
      "name": "lilja",
      "avatar": "https://randomuser.me/api/portraits/women/0.jpg"
    }
  },
  {
    "username": "redswan780",
    "email": "lascívia.dias@example.com",
    "password": "shooter",
    "profile": {
      "name": "lascívia",
      "avatar": "https://randomuser.me/api/portraits/women/95.jpg"
    }
  },
  {
    "username": "silverduck429",
    "email": "alba.benitez@example.com",
    "password": "oakley",
    "profile": {
      "name": "alba",
      "avatar": "https://randomuser.me/api/portraits/women/61.jpg"
    }
  },
  {
    "username": "whitegorilla211",
    "email": "دانیال.سهيليراد@example.com",
    "password": "private",
    "profile": {
      "name": "دانیال",
      "avatar": "https://randomuser.me/api/portraits/men/45.jpg"
    }
  }
];

export default function () {
  users.forEach(function (user) {
    if (typeof Meteor.users.findOne({ username : user.username }) !== 'object') {
      Accounts.createUser(user);
    }
  });
}

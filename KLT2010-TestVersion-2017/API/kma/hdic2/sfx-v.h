/*
	Verb suffix list of KSSM & KSC5601 code.

		N_VSFX = 15, VSFXSIZE = 5 --> defined at 'header/hdics.h'
*/

HAM_UCHAR vsfdic[2][N_VSFX][VSFXSIZE] = {
  {	/* KSSM code for verb suffix */
	{ '\0' },
	{ 0xb7, 0xa1, '\0' },	/* 1:Wi */
	{ 0xd0, 0x61, '\0' },	/* 2:hb */
	{ 0x96, 0x41, '\0' },	/* 3:Gli */
	{ 0xaf, 0x61, 0x9c, 0xf3, '\0' },	/* 4:UzIfR */
	{ 0xaf, 0xa1, 0xc7, 0xa1, '\0' },	/* 5:Uiki */
	{ 0xb7, 0xb6, '\0' },	/* 6:WiV */
	{ 0xb4, 0xf4, '\0' },	/* 7:WfRU */
	{ 0x88, 0x7b, '\0' },	/* 8:Abt */
	{ 0x94, 0x73, '\0' },	/* 9:GbR */
	{ 0x94, 0x77, 0xd0, 0x61, '\0' },	/* 10:GbWhb */
	{ 0xa0, 0x65, 0xd0, 0x61, '\0' },	/* 11:QbDhb */
	{ 0x97, 0x61, 0x9f, 0xa1, '\0' },	/* 12:GzIi */
	{ 0xa4, 0x68, '\0' },	/* 13:RbG */
	{ 'n', 'u', 'l', 'l', '\0' }	/* 14:NULL for ellipsed 'Wi' */
  },
  {	/* KSC5601 code for verb suffix */
	{ '\0' },
	{ 0xc0, 0xcc, '\0' },	/* Wi */
	{ 0xc7, 0xcf, '\0' },	/* hb */
	{ 0xb5, 0xc7, '\0' },	/* Gli */
	{ 0xbd, 0xba, 0xb7, 0xb4, '\0' },	/* UzIfR */
	{ 0xbd, 0xc3, 0xc5, 0xb0, '\0' },	/* Uiki */
	{ 0xc0, 0xd6, '\0' },	/* WiV */
	{ 0xbe, 0xf8, '\0' },	/* WfRU */
	{ 0xb0, 0xb0, '\0' },	/* Abt */
	{ 0xb4, 0xe4, '\0' },	/* GbR */
	{ 0xb4, 0xe7, 0xc7, 0xcf, '\0' },	/* GbWhb */
	{ 0xb8, 0xb8, 0xc7, 0xcf, '\0' },	/* QbDhb */
	{ 0xb5, 0xe5, 0xb8, 0xae, '\0' },	/* GzIi */
	{ 0xb9, 0xde, '\0' },	/* RbG */
	{ 'n', 'u', 'l', 'l', '\0' }	/* 14:NULL for ellipsed 'Wi' */
  }
};


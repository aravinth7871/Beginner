for (int i=0; i<k-1; i++) 
    { 
        int bh = 0; 
        for (int j=0; j<n; j++) 
            if (arr[j] == temp[i].e) 
                bh++; 
        if (bh > n/k) 
           cout << "Number:" << temp[i].e 
                << " Count:" << bh << endl; 
    } 
} 

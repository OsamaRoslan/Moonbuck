# include <stdio.h>
int
main()
{

    int referenceString[10], pageFaults = 0, m, n, s, pages, frames;
printf("\nEnter the number of pages: ");
scanf("%d", & pages);
printf("\nEnter the page references:\n");
for (m = 0; m < pages; m++)
{
    printf("Value[%d]: ", m + 1);
scanf("%d", & referenceString[m]);
}
printf("\nEnter the total number of frames in main memory: ");
{
    scanf("%d", & frames);
}

printf("\n------------Simulation------------");
int
temp[frames];
for (m = 0; m < frames; m++) // initialize
m as -1
to
indicate
that
the
frames
are
not yet
{ // occupied
by
any
page
temp[m] = -1;
}
for (m = 0; m < pages; m++)
{
    s = 0;
for (n = 0; n < frames; n++)
{
// to check if the page is currently in the frame or not
if (referenceString[m] == temp[n])
{
s++;
pageFaults--;
}
}
pageFaults++;
// increment page fault by 1 if the allocation is a miss / invalid

if ((pageFaults <= frames) & & (s == 0))
{
temp[m] = referenceString[m]; // allocate the page to the frame if not yet occupied
}
else if (s == 0)
{
temp[(pageFaults - 1) % frames] = referenceString[m]; // replace the page with a new one
}
printf("\n");
for (n = 0; n < frames; n++)
{
if (temp[n] != -1)
printf(" %d\t\t", temp[n]);
else
printf(" - \t\t");
}
}
printf("\n\nTotal Page Faults: %d\n", pageFaults);
return 0;
}